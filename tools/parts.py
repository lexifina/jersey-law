"""Jersey corpus.d parts: which Laws each part holds, and where their current official consolidation lives.

Each entry: slug, short name, citation (L.n/yyyy), and the page refs the consolidation has been served under on
jerseylaw.je/laws/current/ (the old 'Pages/<chapter>.aspx' form and the newer 'l_<n>_<yyyy>' form).
"""
PARTS = {
    '10-interpretation': [('interpretation', 'Interpretation Law', 'L.17/1954', ['Pages/15.360.aspx', 'l_17_1954'])],
    '20-proceeds-of-crime': [('proceeds-of-crime', 'POCL', 'L.8/1999', ['Pages/08.780.aspx', 'l_8_1999'])],
    '21-misuse-of-drugs': [('misuse-of-drugs', 'Misuse of Drugs Law', 'L.10/1978', ['Pages/08.680.aspx', 'l_10_1978'])],
    '22-terrorism': [('terrorism', 'Terrorism Law', 'L.40/2002', ['Pages/17.850.aspx', 'l_40_2002'])],
    '23-police-procedures': [('police-procedures', 'PPCE Law', 'L.5/2003', ['Pages/23.750.aspx', 'l_5_2003'])],
    '30-companies': [('companies', 'Companies Law', 'L.30/1991', ['Pages/13.125.aspx', 'l_30_1991'])],
    '31-employment': [('employment', 'EL', 'L.42/2003', ['Pages/05.255.aspx', 'l_42_2003'])],
    '32-criminal-procedure': [('criminal-procedure', 'Criminal Procedure Law', 'L.25/2018', ['l_25_2018'])],
    '33-sexual-offences': [('sexual-offences', 'Sexual Offences Law', 'L.20/2018', ['l_20_2018'])],
    '34-human-rights': [('human-rights', 'HRL', 'L.19/2000', ['Pages/15.350.aspx', 'l_19_2000'])],
    '35-data-protection': [('data-protection', 'DPL', 'L.3/2018', ['Pages/15.240.aspx', 'l_3_2018'])],
}

BASE = 'https://www.jerseylaw.je/laws/current/'


def current_url(cite):
    n, y = cite[2:].split('/')
    return f'{BASE}l_{n}_{y}'


def all_acts():
    for part, acts in PARTS.items():
        for a in acts:
            yield part, a


def matches(url, refs):
    """Whether an archived URL is one of this Law's current-consolidation pages (any host form, any case)."""
    u = url.split('://', 1)[-1].lower().split('?', 1)[0].split('#', 1)[0]
    u = u[4:] if u.startswith('www.') else u
    return any(u == ('jerseylaw.je/laws/current/' + r).lower() for r in refs)
