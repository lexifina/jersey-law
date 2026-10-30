"""Jersey: build corpus.d parts from cached official consolidations (deterministic, cache only).

Each Law's versions are the official consolidations published on jerseylaw.je/laws/current/, one per "Showing the law
from" day: the current page plus earlier copies of the same page. A unit that changed between two versions is credited
to an amending law only when that version's own endnotes name the law for that Article or Schedule AND the version's
"from" day is one of that law's commencement days in the page's Table of Legislation History (or, for a Law Revision
Board item, the day the endnote says the text was revised). Anything else stays unexplained.
"""
import hashlib, html, json, os, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
from parse import parse_raw, clean, MONTHS  # noqa: E402
from parts import PARTS, current_url  # noqa: E402

CACHE = HERE / '.cache'
DATE = re.compile(r'(\d{1,2})\s+([A-Z][a-z]+)\s+(\d{4})')


def iso(m):
    mon = MONTHS.get(m.group(2).lower()[:3])
    return f'{int(m.group(3)):04d}-{mon:02d}-{int(m.group(1)):02d}' if mon else None


def law_key(cite):
    c = cite.replace('&amp;', '&')
    m = re.match(r'L\.(\d+)/(\d{4})$', c)
    if m:
        return f'l-{int(m.group(1))}-{m.group(2)}'
    m = re.match(r'R&O\.(\d+)(?:/(\d{4}))?$', c)
    if m:
        return f'ro-{int(m.group(1))}' + (f'-{m.group(2)}' if m.group(2) else '')
    return None


def history(t):
    """Table of Legislation History: {cite: (title, [commencement days])}."""
    m = re.compile(r'Table\s+of\s+Legislation\s+History').search(t, max(t.find('iLAWS600EndnotesTitle'), 0))
    if not m:
        return {}
    b = t[m.start():]
    e = re.search(r'Table\s+of\s+(?:Renumbered|Endnote)', b[30:])
    j = e.start() + 30 if e else len(b)
    out = {}
    for tr in re.findall(r'<tr[^>]*>(.*?)</tr>', b[:j], re.S):
        cells = [clean(c) for c in re.findall(r'<td[^>]*>(.*?)</td>', tr, re.S)]
        if len(cells) < 3:
            continue
        cite = cells[1].replace(' ', '')
        if not law_key(cite):
            continue
        days = [d for d in (iso(m) for m in DATE.finditer(cells[2])) if d]
        out[cite.replace('&amp;', '&')] = (cells[0], days)
    return out


def target_key(target):
    """'Article 11A(3)' -> art-011-a; 'Schedule' / 'Schedule 2 paragraph 1' -> sch-01 / sch-02."""
    m = re.match(r'Articles?\s+(\d+)([A-Z]{0,3})\b', target)
    if m:
        return f'art-{int(m.group(1)):03d}' + (f'-{m.group(2).lower()}' if m.group(2) else '')
    m = re.match(r'Schedules?(?:\s+(\d+))?', target)
    if m:
        return f'sch-{int(m.group(1) or 1):02d}'
    return None


def endnotes(t):
    """{unit key: [(cite or 'LRB:<item>', revised day or None)]} from the Table of Endnote References."""
    out = {}
    for body in re.findall(r'<div[^>]*id="edn\d+"[^>]*>(.*?)</div>', t, re.S):
        x = clean(body)
        x = re.sub(r'^\[\d+\]\s*', '', x)
        k = target_key(x)
        if not k:
            continue
        for c in re.findall(r'(L\.\d+/\d{4}|R&(?:amp;)?O\.\d+(?:/\d{4})?)', x):
            out.setdefault(k, []).append((c.replace('&amp;', '&'), None))
        for m in re.finditer(r'revised\s+on\s+(\d{1,2}\s+[A-Z][a-z]+\s+\d{4})\s+by\s+Law\s+Revision\s+Board\s+item\s+(\d{4}/\d+)', x):
            out.setdefault(k, []).append((f'LRB:{m.group(2)}', iso(DATE.search(m.group(1)))))
    return out


def load_versions(slug, cite):
    """[(from, body bytes, capture date)] newest capture per 'from' day, ordered by from."""
    idx = json.loads((CACHE / 'parts_index.json').read_text(encoding='utf8'))
    by_from = {}
    for r in idx.get(slug, []):
        raw = (CACHE / 'bodies' / r['sha256']).read_bytes()
        if not (raw.rstrip().endswith(b'</html>') and b'iLAWS600EndnotesTitle' in raw):
            continue  # an incomplete copy (cut off before the endnotes) would read as deleted provisions
        try:
            title, frm, units = parse_raw(raw)
        except Exception:
            continue
        if not units:
            continue
        ts = r['timestamp']
        cap = '9999' if ts == 'live' else ts
        if frm not in by_from or cap > by_from[frm][2]:
            by_from[frm] = (title, raw, cap, units)
    def norm(x):
        return re.sub(r'\s+', ' ', x).strip().lower()
    newest = by_from[max(by_from, key=lambda f: by_from[f][2])][0] if by_from else None
    # an old page address can have held a different Law (chapter numbers were reassigned): keep this Law's pages only
    return [(f,) + by_from[f] for f in sorted(by_from) if norm(by_from[f][0]) == norm(newest)]


def build_part(part, acts):
    laws, out_acts, decisions = {}, [], []
    for slug, short, cite, refs in acts:
        vers = load_versions(slug, cite)
        if not vers:
            print(slug, 'no versions', file=sys.stderr)
            continue
        own = law_key(cite)
        url = current_url(cite)
        title_now = vers[-1][1]
        laws[own] = {'label': title_now, 'title': title_now, 'kind': 'law', 'enacted': None, 'published': None,
                     'url': url, 'temporary_until': None, 'restores': None,
                     'note': f'{cite}; as first enacted. The oldest version published as text here is an official consolidation.'}
        versions, prev = [], None
        for frm, title, raw, cap, units in vers:
            t = raw.decode('utf8', 'replace')
            seen = 'retrieved 2026-10-30' if cap == '9999' else f'as published on {cap[:4]}-{cap[4:6]}-{cap[6:8]}'
            v = {'from': frm, 'source_url': url, 'sha256': hashlib.sha256(raw).hexdigest(), 'units': units,
                 'credits': {}, 'note': f'Official consolidated version showing the law from {frm} (jerseylaw.je, {seen}).'}
            if prev is not None:
                hist, ends = history(t), endnotes(t)
                pend = endnotes(prev[1])
                changed = sorted(k for k in set(units) | set(prev[0]) if units.get(k) != prev[0].get(k))
                for k in changed:
                    cr = []
                    for c, rev in ends.get(k, []) + pend.get(k, []):
                        if c.startswith('LRB:'):
                            if rev == frm:
                                key = 'lrb-' + c[4:].replace('/', '-')
                                laws[key] = {'label': f'Law Revision Board item {c[4:]}', 'title': f'Law Revision Board item {c[4:]} (revision under the Legislation (Jersey) Law 2021)',
                                             'kind': 'publisher', 'enacted': frm, 'published': None, 'url': None,
                                             'temporary_until': None, 'restores': None, 'note': None}
                                cr.append(key)
                        elif c in hist and frm in hist[c][1]:
                            key = law_key(c)
                            laws[key] = {'label': hist[c][0], 'title': hist[c][0], 'kind': 'decree' if c.startswith('R&O') else 'law',
                                         'enacted': None, 'published': None, 'url': None,
                                         'temporary_until': None, 'restores': None, 'note': f'{c}; in force {", ".join(hist[c][1])} (Table of Legislation History).'}
                            cr.append(key)
                    if cr:
                        v['credits'][k] = sorted(set(cr))
            versions.append(v)
            prev = (units, t)
        out_acts.append({'slug': slug, 'short': short, 'title': title_now, 'url': url, 'first_law': None,
                         'earlier_laws': [own], 'versions': versions})
        decisions.append(f'{title_now}: {len(versions)} official consolidations, one per "Showing the law from" day; '
                         'a changed Article or Schedule is credited to an amending law only where that version\'s endnotes '
                         'name the law for it and the version\'s day is one of the law\'s commencement days in its Table of '
                         'Legislation History; otherwise it is left unexplained.')
        print(slug, [v['from'] for v in versions], sum(len(v['credits']) for v in versions), 'credited units')
    part_doc = {'laws': laws, 'acts': out_acts, 'decisions': decisions}  # the source is listed once, in corpus.json
    d = Path(os.environ.get('JE_OUT', HERE)) / 'corpus.d'
    d.mkdir(exist_ok=True)
    p = d / f'{part}.json'
    tmp = p.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(part_doc, ensure_ascii=False, indent=1) + '\n', encoding='utf8', newline='\n')
    tmp.replace(p)


def main(only=None):
    for part, acts in PARTS.items():
        if only and part not in only:
            continue
        build_part(part, acts)


if __name__ == '__main__':
    main(set(sys.argv[1:]) or None)
