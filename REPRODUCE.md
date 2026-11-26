# How this repository was made (Jersey)

## Sources

| Source | Address | Licence | Used for |
| --- | --- | --- | --- |
| Jersey Law, Jersey Legal Information Board | <https://www.jerseylaw.je/laws/current> | Open States Assembly Licence (OSAL-J) v.1 | The current official consolidation of each Law, R&O and Order in Council, its "Showing the law from" day and its Table of Legislation History |
| Jersey Law, Laws as Enacted | <https://www.jerseylaw.je/laws/enacted> | OSAL-J v.1 | Each Law as enacted |
| Wayback Machine CDX listing (archive.org) | <https://web.archive.org/cdx/search/cdx?url=jerseylaw.je/laws/current/&matchType=prefix> | listing only | The list of page addresses to start from; no page text is taken from it |

Earlier versions of 11 Laws (2020-11-25 onwards) came from earlier copies of the same current-law pages (Common
Crawl), built by the earlier pipeline (`tools/`).

## Method

- `runner/je_fetch.py` reads each current-law page (`/laws/current/<id>`) once, one request at a time about 1.5 s
  apart, and follows the links between pages to find the rest; for each Law it also reads the as-enacted page its
  Table of Legislation History links. Search pages are not scraped. robots.txt disallows `/laws/enacted/`; it is read
  anyway at the same slow pace because the Greffier licenses that text for re-use (robots.txt is treated as advisory).
  `/laws/revised/` (point-in-time versions) and judgments are outside the OSAL-J licence and are not read.
- `runner/je_parse.py` splits each page into Articles, Regulations, Rules and Schedules; `runner/je_build.py` writes
  one commit per version (see STRUCTURE.md for the dating rules) and pushes fast-forward only.
- The publisher asks bulk users to request its REST API; the record was read page by page at the pace above.

## Counts

40 Laws, 0 Regulations and Orders, 0 Orders in Council. 14 pages or as-enacted versions held:

| Page | Why held |
| --- | --- |
| `enacted:l_10_1960` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_1961` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_18_2022` | commenced in stages or no day ("4 April 2022 Adopted Law given effect as if enacted on 10 February 2022 by R&O.1") |
| `enacted:l_20_2022` | commenced in stages ("24 June 2022 (Articles 15 and 16 only) 1 January 2024 (all remaining provisions ") |
| `enacted:l_22_2026` | commenced in stages ("1 September 2026 - Parts 1, 2, 3 and 7 and Schedules 1, 2 and 4 (R&O.86/2026) No") |
| `enacted:l_25_2009` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_26_1999` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_29_1993` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_35_2026` | commenced in stages ("17 July 2026 - Articles 1, 36 to 39, 41(1)(c) and (2), 43 to 105, Schedules 1 an") |
| `enacted:l_50_2002` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_7_2025` | commenced in stages or no day ("1 January 2025 Adopted Law given effect as if enacted on 22 October 2024 by R&O.") |
| `enacted:l_8_1990` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_8_2005` | commenced in stages ("11 March 2005 - Articles 1, 47, 48, 49 and 53 26 July 2005 - Article 6, Article ") |
| `enacted:l_8_2025` | commenced in stages or no day ("1 January 2025 Adopted Law given effect as if enacted on 22 October 2024 by R&O.") |
