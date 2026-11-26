# How this repository was made (Jersey)

## Sources

| Source | Address | Licence | Used for |
| --- | --- | --- | --- |
| Jersey Law, Jersey Legal Information Board | <https://www.jerseylaw.je/laws/current> | Open States Assembly Licence (OSAL-J) v.1 | The current official consolidation of each Law, R&O and Order in Council, the point-in-time versions its timeline lists, each version's "Showing the law from" day and its Table of Legislation History |
| Jersey Law, Laws as Enacted | <https://www.jerseylaw.je/laws/enacted> | OSAL-J v.1 | Each Law as enacted |
| Wayback Machine CDX listing (archive.org) | <https://web.archive.org/cdx/search/cdx?url=jerseylaw.je/laws/current/&matchType=prefix> | listing only | The list of page addresses to start from; no page text is taken from it |

Versions of 11 Laws from 2020-11-25 to 2026-10-02 came from earlier copies of the same current-law pages (Common
Crawl), built by the earlier pipeline (`tools/`).

## Method

- `runner/je_fetch.py` reads each current-law page (`/laws/current/<id>`) and each point-in-time version its
  timeline lists (`/laws/current/<id>_<yyyymmdd>`), one request at a time 3 s apart (the host answers 503 when
  faster), and follows the links between pages to find the rest; for each Law it also reads the as-enacted page its
  Table of Legislation History links. Search pages are not scraped. robots.txt disallows `/laws/enacted/`; it is read
  anyway at the same slow pace because the Greffier licenses that text for re-use (robots.txt is treated as advisory).
  `/laws/revised/` and judgments are outside the OSAL-J licence and are not read.
- `runner/je_parse.py` splits each page into Articles, Regulations, Rules and Schedules; `runner/je_build.py` writes
  one commit per version (see STRUCTURE.md for the dating rules) and pushes fast-forward only.
- The publisher asks bulk users to request its REST API; the record was read page by page at the pace above.

## Counts

120 Laws, 0 Regulations and Orders, 0 Orders in Council. 52 pages or versions held:

| Page | Why held |
| --- | --- |
| `enacted:l_10_1960` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_10_2017` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_10_2019` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_11_2016` | commenced in stages ("1 January 2017: Parts 1, 12 and 13, specified provisions in Parts 14, 15 and spe") |
| `enacted:l_11_2019` | commenced in stages ("22 July 2021 - except Articles 2 to 5 and 10 to 23 (R&O.91/2021) 1 April 2022 - ") |
| `enacted:l_12_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_13_2016` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_13_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_13_2019` | commenced in stages ("1 January 2020 - except Articles 17, 18, 19 (R&O.136/2019) Not in force - Articl") |
| `enacted:l_14_2005` | commenced in stages ("14 September 2005, Articles 1, 40 to 45, 69 and 71 to 74 (R&O.97/2005) 9 Decembe") |
| `enacted:l_16_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_1961` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_2015` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_2017` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_2018` | commenced in stages ("19 September 2018 (Articles 1, 4, 5, 8, 9, 10 and 11 only) See R&O.93/2018 19 Ju") |
| `enacted:l_18_2022` | commenced in stages or no day ("4 April 2022 Adopted Law given effect as if enacted on 10 February 2022 by R&O.1") |
| `enacted:l_1_2017` | commenced in stages ("17 July 2017, except Articles 10(1)(d); 20 and 30(3) (R&O.72/2017) 16 December 2") |
| `enacted:l_1_2019` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_20_2017` | commenced in stages ("24 July 2019 - except substituted Article 30(10)(b) of the Police Procedures and") |
| `enacted:l_20_2018_20191008` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_20_2022` | commenced in stages ("24 June 2022 (Articles 15 and 16 only) 1 January 2024 (all remaining provisions ") |
| `enacted:l_22_2026` | commenced in stages ("1 September 2026 - Parts 1, 2, 3 and 7 and Schedules 1, 2 and 4 (R&O.86/2026) No") |
| `enacted:l_24_2005` | commenced in stages ("26 August 2005 as to Articles 1, 5(1) and 7 and Part 1 of Schedule 2 6 December ") |
| `enacted:l_25_2009` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_25_2017` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_26_1999` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_26_2004` | commenced in stages ("11 October 2004 as to Parts 1, 3, 4, 5, 6 and 11; Articles 31, 32, 34-42, 71-75,") |
| `enacted:l_26_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_27_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_29_1993` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_2_2017` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_2_2019` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_30_2012` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_32_2018` | commenced in stages ("1 September 2022 (except Article 12) (R&O.39/2022)") |
| `enacted:l_35_2026` | commenced in stages ("17 July 2026 - Articles 1, 36 to 39, 41(1)(c) and (2), 43 to 105, Schedules 1 an") |
| `enacted:l_3_2007` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_3_2018_20230505` | commenced in stages ("25 May 2018, except as follows Part 5, 25 November 2018 Articles 17 and 18, 25 M") |
| `enacted:l_3_2019` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_41_2008` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_4_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_4_2017` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_4_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_50_2002` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_6_2010` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_6_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_6_2016` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_7_2025` | commenced in stages or no day ("1 January 2025 Adopted Law given effect as if enacted on 22 October 2024 by R&O.") |
| `enacted:l_8_1990` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_8_2005` | commenced in stages ("11 March 2005 - Articles 1, 47, 48, 49 and 53 26 July 2005 - Article 6, Article ") |
| `enacted:l_8_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_8_2019` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_8_2025` | commenced in stages or no day ("1 January 2025 Adopted Law given effect as if enacted on 22 October 2024 by R&O.") |
