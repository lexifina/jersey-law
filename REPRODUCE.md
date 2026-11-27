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

393 Laws, 465 Regulations and Orders, 0 Orders in Council. 603 pages or versions held:

| Page | Why held |
| --- | --- |
| `enacted:l_10_1960` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_10_2008` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_10_2009` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_10_2017` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_10_2019` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_11_1998` | commenced in stages ("4 June 1998; except for (original) Articles 5, 6, 7, 9, 22, 23 in force 1 July 1") |
| `enacted:l_11_2003` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_11_2010` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_11_2016` | commenced in stages ("1 January 2017: Parts 1, 12 and 13, specified provisions in Parts 14, 15 and spe") |
| `enacted:l_11_2019` | commenced in stages ("22 July 2021 - except Articles 2 to 5 and 10 to 23 (R&O.91/2021) 1 April 2022 - ") |
| `enacted:l_12_2002` | commenced in stages ("5 June 2002 (R&O.42/2002) - except Articles 6(6), 7(1) to (3) and (5), 12(2)(b) ") |
| `enacted:l_12_2006` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_12_2013` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_12_2016` | commenced in stages ("1 February 2017 (R&O.2/2017) (paragraphs 2(b) and (c) and 17(a) of Schedule 5 in") |
| `enacted:l_12_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_13_2016` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_13_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_13_2019` | commenced in stages ("1 January 2020 - except Articles 17, 18, 19 (R&O.136/2019) Not in force - Articl") |
| `enacted:l_14_2000` | commenced in stages or no day ("2 June 2000, 26 November 2000") |
| `enacted:l_14_2003` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_14_2005` | commenced in stages ("14 September 2005, Articles 1, 40 to 45, 69 and 71 to 74 (R&O.97/2005) 9 Decembe") |
| `enacted:l_14_2009` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_14_2012` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_14_2014` | commenced in stages ("25 July 2014 - Parts 1, 2 and 6 and Schedules 1 and 2 25 November 2014 (R&O.186/") |
| `enacted:l_15_1967` | commenced in stages ("1 June 1968 except Schedule 3 Part 6(5) and Part 11 which commence 1 January 197") |
| `enacted:l_15_2008` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_15_2016` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_16_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_1961` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_2004` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_2005` | commenced in stages ("10 December 2006 (except paragraph 2 of Schedule 4) (R&O.142/2006)") |
| `enacted:l_17_2011` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_2015` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_2017` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_17_2018` | commenced in stages ("19 September 2018 (Articles 1, 4, 5, 8, 9, 10 and 11 only) See R&O.93/2018 19 Ju") |
| `enacted:l_18_1962` | commenced in stages ("19 September 1962 (Articles 1, 19-22), 1 December 1962 (Articles 5, 6, 8, 9(1)(a") |
| `enacted:l_18_2006` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_18_2010` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_18_2014` | commenced in stages ("1 January 2016 - whole Law except Articles 10(4) to (8) and 11; 1 January 2019 -") |
| `enacted:l_18_2022` | commenced in stages or no day ("4 April 2022 Adopted Law given effect as if enacted on 10 February 2022 by R&O.1") |
| `enacted:l_1_1934` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_1_2002` | commenced in stages ("1 July 2002 - Parts 1, 3, 4, 5, 7 and 8, Articles 54 to 61, Articles 63 to 65, A") |
| `enacted:l_1_2009` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_1_2010` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_1_2012` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_1_2017` | commenced in stages ("17 July 2017, except Articles 10(1)(d); 20 and 30(3) (R&O.72/2017) 16 December 2") |
| `enacted:l_1_2019` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_20_2012` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_20_2017` | commenced in stages ("24 July 2019 - except substituted Article 30(10)(b) of the Police Procedures and") |
| `enacted:l_20_2018_20191008` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_20_2022` | commenced in stages ("24 June 2022 (Articles 15 and 16 only) 1 January 2024 (all remaining provisions ") |
| `enacted:l_21_2010` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_21_2012` | commenced in stages ("Parts 1, 2 and 5 and Articles 16 and 18 - 12 December 2013; Parts 3 and 4 and Ar") |
| `enacted:l_22_1949` | commenced in stages ("15 March 1950 (R&O.2594), (Articles 1, 2, 4, 5(1), 43, 44 and 47 in force 17 Jan") |
| `enacted:l_22_2026` | commenced in stages ("1 September 2026 - Parts 1, 2, 3 and 7 and Schedules 1, 2 and 4 (R&O.86/2026) No") |
| `enacted:l_23_1962` | commenced in stages ("Articles 1, 6, 7, 17, 18, 19, 21 in force 1 December 1962, remainder in force 1 ") |
| `enacted:l_23_2009` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_23_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_24_2004` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_24_2005` | commenced in stages ("26 August 2005 as to Articles 1, 5(1) and 7 and Part 1 of Schedule 2 6 December ") |
| `enacted:l_24_2012` | commenced in stages ("1 October 2013 - Articles 1 to 4A, 8, 9, 14(1), 60 to 84, 90 to 93, 95 and 96, a") |
| `enacted:l_24_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_25_2009` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_25_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_25_2017` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_26_1999` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_26_2004` | commenced in stages ("11 October 2004 as to Parts 1, 3, 4, 5, 6 and 11; Articles 31, 32, 34-42, 71-75,") |
| `enacted:l_26_2005` | commenced in stages ("28 October 2005, Articles 1, 39 and 40, 9 December 2005, remainder (R&O.156/2005") |
| `enacted:l_26_2011` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_26_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_26_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_27_1999` | commenced in stages ("1 March 2000 (except Articles 37, 38, 39(3) and (4) and 40 to 44 commence 1 Janu") |
| `enacted:l_27_2004` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_27_2005` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_27_2007` | commenced in stages ("17 August 2007, as to Part 1, Articles 97 to 102, Schedule 2 and so much of any ") |
| `enacted:l_27_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_27_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_28_1952` | commenced in stages or no day ("1 January 1953 and 17 October 1952 (R&O.3189)") |
| `enacted:l_28_1969` | commenced in stages or no day ("17 November 1969 (for making Orders) 3 July 1970 for all other purposes") |
| `enacted:l_28_2004` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_28_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_29_1993` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_29_2007` | commenced in stages ("1 January 2009 except Article 11 and paragraph 3 of Schedule 3 (originally 4) in") |
| `enacted:l_29_2008` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_29_2011` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_29_2016` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_2_1905` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_2_1948` | commenced in stages ("22 September 1948 (Articles 1-3, 32, 35, 36), 1 October 1948 (Articles 5, 6, 10,") |
| `enacted:l_2_2017` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_2_2019` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_30_2003` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_30_2008` | commenced in stages ("8 August 2008, except Article 24 in force 8 November 2008") |
| `enacted:l_30_2012` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_30_2016` | commenced in stages ("1 October 2018 - except Article 67(1)(a) and (2) 1 January 2019 - Article 67(1)(") |
| `enacted:l_31_2008` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_31_2011` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_31_2012` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_32_1998` | commenced in stages or no day ("1 March 1999, (1 July 1999 for Art. 6) (R&O.9356)") |
| `enacted:l_32_2003` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_32_2008` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_32_2018` | commenced in stages ("1 September 2022 (except Article 12) (R&O.39/2022)") |
| `enacted:l_33_1999` | commenced in stages ("1 November 2000 (R&O.92/2000) except - 7 December 2006, Article 19 and the part ") |
| `enacted:l_33_2005` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_35_2008` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_35_2012` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_35_2026` | commenced in stages ("17 July 2026 - Articles 1, 36 to 39, 41(1)(c) and (2), 43 to 105, Schedules 1 an") |
| `enacted:l_36_2002` | commenced in stages ("1 July 2006 (R&O.49/2006) except - 31 March 2007, as to Articles 22(1)(b), 109(2") |
| `enacted:l_36_2007` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_37_2007` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_37_2012` | commenced in stages ("24 July 2013 - Articles 1, 2, 3(1) to (4), 4 to 7, 17(1) to (4), 18 to 20 and 34") |
| `enacted:l_37_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_39_2007` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_3_2005` | commenced in stages ("28 January 2005, except Article 4") |
| `enacted:l_3_2007` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_3_2018_20230505` | commenced in stages ("25 May 2018, except as follows Part 5, 25 November 2018 Articles 17 and 18, 25 M") |
| `enacted:l_3_2019` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_41_2008` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_41_2014` | commenced in stages ("Parts 1 to 3, Articles 32, 38, 39, 40, 42, 43 and 44 and the Schedules, in force") |
| `enacted:l_42_2014` | commenced in stages ("15 November 2014 as to Articles 1, 2, 3(6), 10, 11, 14 to 16, 30(3), 35 to 43, 4") |
| `enacted:l_4_2008` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_4_2012` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_4_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_4_2017` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_4_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_50_2002` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_5_1948` | commenced in stages ("1 November 1948 (Articles 1 and 16 to 21) 1 January 1949 (Articles 2 to 15) (R&O") |
| `enacted:l_5_1974` | commenced in stages or no day ("17 May 1974, 18 September 1974 (R&O.6042)") |
| `enacted:l_5_2011` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_6_1951` | commenced in stages ("5 May 1951 (Article 9, 2 February 1952, R&O.3038)") |
| `enacted:l_6_1988` | commenced in stages ("1 June 1988, (1 June 1989 for Article 4) (R&O.7757)") |
| `enacted:l_6_1997` | commenced in stages ("1 August 1997, Schedule 3, paragraph 2(1)(b) in force 1 January 1999 (R&O.9096)") |
| `enacted:l_6_2005` | commenced in stages ("1 May 2005 (except Parts 2 and 3) 1 November 2005 (Parts 2 and 3) (R&O.22/2005)") |
| `enacted:l_6_2010` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_6_2011` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_6_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_6_2016` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_7_1949` | commenced in stages or no day ("1 August 1949 (Art. 22 in force 6 July 1949) (R&O.2421)") |
| `enacted:l_7_2005` | commenced in stages ("1 November 2006, except - 1 February 2007 (Articles 23, 38 and 49, Part 4, Artic") |
| `enacted:l_7_2009` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_7_2014` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_7_2025` | commenced in stages or no day ("1 January 2025 Adopted Law given effect as if enacted on 22 October 2024 by R&O.") |
| `enacted:l_8_1948` | commenced in stages ("15 January 1949 (original Articles 13, 14, 15 in force 1 February 1965 R&O.4617)") |
| `enacted:l_8_1990` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_8_2005` | commenced in stages ("11 March 2005 - Articles 1, 47, 48, 49 and 53 26 July 2005 - Article 6, Article ") |
| `enacted:l_8_2010` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_8_2011` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_8_2015` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_8_2018` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_8_2019` | as-enacted page not in the current format (no Articles found) |
| `enacted:l_8_2025` | commenced in stages or no day ("1 January 2025 Adopted Law given effect as if enacted on 22 October 2024 by R&O.") |
| `enacted:l_9_2005` | commenced in stages ("1 January 2007 (R&O.136/2006) - except 1 April 2007 as to Article 3(2) and (3)") |
| `enacted:l_9_2007` | commenced in stages ("28 January 2008 (R&O.128/2007), except paragraph 3(b) of Schedule 1, not in forc") |
| `enacted:l_9_2015` | commenced in stages ("8 September 2015 - Articles 1 (for specified purposes), 3, 13 (for specified pur") |
| `l_1_1813` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `l_1_1832` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `l_2_1840` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `l_3_1884` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_13_2001` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_1_1771` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_28_1973` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_2_1869` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_2_1884` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_32_1997` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_3_1931` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_4_1851` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_5_1900` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_5_1986` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_6_1998` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_9_1967` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `oinc_9_1970` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `pit:l_10_1937` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_10_1953` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_10_1957` | point-in-time versions before 2026-08-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_10_1958` | point-in-time versions before 2026-08-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_10_1978` | point-in-time versions before 2025-12-05 not added: the folder was published before they were read (history is append-only) |
| `pit:l_10_1994` | point-in-time versions before 2021-10-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_10_2008` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_10_2009` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_10_2013` | point-in-time versions before 2026-04-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_10_2017` | point-in-time versions before 2026-07-06 not added: the folder was published before they were read (history is append-only) |
| `pit:l_10_2019` | point-in-time versions before 2026-07-16 not added: the folder was published before they were read (history is append-only) |
| `pit:l_11_1955` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_11_1957` | point-in-time versions before 2026-08-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_11_1984` | point-in-time versions before 2026-03-20 not added: the folder was published before they were read (history is append-only) |
| `pit:l_11_1996` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_11_1998` | point-in-time versions before 2025-12-04 not added: the folder was published before they were read (history is append-only) |
| `pit:l_11_2003` | point-in-time versions before 2024-12-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_11_2010` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_11_2014` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_11_2016` | point-in-time versions before 2024-12-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_11_2019` | point-in-time versions before 2024-12-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_1952` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_1956` | point-in-time versions before 2025-06-18 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_1960` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_1967` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_1990` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_1994` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_1996` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_2001` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_2002` | point-in-time versions before 2026-06-07 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_2006` | point-in-time versions before 2025-04-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_2013` | point-in-time versions before 2019-07-23 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_2016` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_2018` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_12_2021` | point-in-time versions before 2025-06-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_13_1966` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_13_1974` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_13_1991` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_13_2002` | point-in-time versions before 2025-06-18 not added: the folder was published before they were read (history is append-only) |
| `pit:l_13_2019` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_14_1960` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_14_1962` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_14_1967` | point-in-time versions before 2022-09-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_14_1999` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_14_2000` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_14_2003` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_14_2009` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_14_2012` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_14_2014` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_14_2022` | point-in-time versions before 2025-10-29 not added: the folder was published before they were read (history is append-only) |
| `pit:l_15_1952` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_15_1963` | point-in-time versions before 2021-10-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_15_1965` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_15_1967` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_15_1972` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_15_1984` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_15_2000` | point-in-time versions before 2023-04-12 not added: the folder was published before they were read (history is append-only) |
| `pit:l_15_2008` | point-in-time versions before 2022-04-29 not added: the folder was published before they were read (history is append-only) |
| `pit:l_15_2016` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_15_2021` | point-in-time versions before 2026-02-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_16_1954` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_16_1998` | point-in-time versions before 2026-06-12 not added: the folder was published before they were read (history is append-only) |
| `pit:l_16_2018` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_16_2025` | point-in-time versions before 2025-11-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_1952` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_1954` | point-in-time versions before 2026-06-19 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_1956` | point-in-time versions before 2025-12-04 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_1959` | point-in-time versions before 2019-07-23 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_1961` | point-in-time versions before 2025-04-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_1963` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_1973` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_1997` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_2004` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_2005` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_2011` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_2014` | point-in-time versions before 2026-02-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_2017` | point-in-time versions before 2026-03-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_17_2018` | point-in-time versions before 2020-12-31 not added: the folder was published before they were read (history is append-only) |
| `pit:l_18_1960` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_18_1962` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_18_1973` | point-in-time versions before 2019-03-13 not added: the folder was published before they were read (history is append-only) |
| `pit:l_18_1989` | point-in-time versions before 2022-08-12 not added: the folder was published before they were read (history is append-only) |
| `pit:l_18_1993` | point-in-time versions before 2026-06-12 not added: the folder was published before they were read (history is append-only) |
| `pit:l_18_2006` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_18_2010` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_18_2014` | point-in-time versions before 2025-04-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_18_2022` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_19_1991` | point-in-time versions before 2026-07-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_19_1994` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_19_2000` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_19_2005` | point-in-time versions before 2026-04-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_19_2011` | point-in-time versions before 2022-03-25 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_1804` | point-in-time versions before 2022-01-20 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_1862` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_1864` | point-in-time versions before 2020-03-25 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_1880` | point-in-time versions before 2026-06-12 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_1925` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_1951` | point-in-time versions before 2026-02-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_1957` | point-in-time versions before 2026-08-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_1971` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_2002` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_2009` | point-in-time versions before 2026-06-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_2010` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_2012` | point-in-time versions before 2024-06-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_2017` | point-in-time versions before 2025-06-18 not added: the folder was published before they were read (history is append-only) |
| `pit:l_1_2019` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_20_1962` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_20_1990` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_20_2012` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_20_2017` | point-in-time versions before 2026-07-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_20_2018` | point-in-time versions before 2026-04-06 not added: the folder was published before they were read (history is append-only) |
| `pit:l_20_2022` | point-in-time versions before 2026-07-16 not added: the folder was published before they were read (history is append-only) |
| `pit:l_21_1960` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_21_1974` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_21_2010` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_21_2012` | point-in-time versions before 2023-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_22_1949` | point-in-time versions before 2026-04-06 not added: the folder was published before they were read (history is append-only) |
| `pit:l_22_1961` | point-in-time versions before 2022-04-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_22_1965` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_22_1973` | point-in-time versions before 2021-07-31 not added: the folder was published before they were read (history is append-only) |
| `pit:l_22_1974` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_22_1994` | point-in-time versions before 2026-04-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_22_2001` | point-in-time versions before 2019-05-03 not added: the folder was published before they were read (history is append-only) |
| `pit:l_22_2026` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_23_1950` | point-in-time versions before 2026-04-15 not added: the folder was published before they were read (history is append-only) |
| `pit:l_23_1952` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_23_1957` | point-in-time versions before 2025-06-18 not added: the folder was published before they were read (history is append-only) |
| `pit:l_23_1961` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_23_1962` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_23_2009` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_23_2014` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_24_1973` | point-in-time versions before 2022-09-08 not added: the folder was published before they were read (history is append-only) |
| `pit:l_24_1974` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_24_1995` | point-in-time versions before 2023-02-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_24_2004` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_24_2012` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_24_2014` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_25_1960` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_25_2014` | point-in-time versions before 2026-10-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_25_2017` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_25_2018` | point-in-time versions before 2026-08-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_26_1956` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_26_1964` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_26_1993` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_26_2005` | point-in-time versions before 2026-10-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_26_2011` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_26_2014` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_26_2018` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_27_1999` | point-in-time versions before 2025-06-05 not added: the folder was published before they were read (history is append-only) |
| `pit:l_27_2002` | point-in-time versions before 2021-10-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_27_2004` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_27_2005` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_27_2007` | point-in-time versions before 2026-04-06 not added: the folder was published before they were read (history is append-only) |
| `pit:l_27_2014` | point-in-time versions before 2026-08-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_27_2018` | point-in-time versions before 2025-06-18 not added: the folder was published before they were read (history is append-only) |
| `pit:l_27_2022` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_28_1952` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_28_1969` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_28_2004` | point-in-time versions before 2020-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_28_2005` | point-in-time versions before 2025-04-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_28_2014` | point-in-time versions before 2023-04-12 not added: the folder was published before they were read (history is append-only) |
| `pit:l_29_1961` | point-in-time versions before 2026-06-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_29_1998` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_29_2005` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_29_2007` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_29_2008` | point-in-time versions before 2022-09-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_29_2011` | point-in-time versions before 2026-08-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_29_2016` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_2_1891` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_2_1947` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_2_1948` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_2_1957` | point-in-time versions before 2019-07-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_2_1958` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_2_1967` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_2_2017` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_2_2019` | point-in-time versions before 2026-03-18 not added: the folder was published before they were read (history is append-only) |
| `pit:l_2_2020` | point-in-time versions before 2022-05-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_30_1991` | point-in-time versions before 2026-09-30 not added: the folder was published before they were read (history is append-only) |
| `pit:l_30_2003` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_30_2008` | point-in-time versions before 2025-12-04 not added: the folder was published before they were read (history is append-only) |
| `pit:l_30_2012` | point-in-time versions before 2022-01-20 not added: the folder was published before they were read (history is append-only) |
| `pit:l_30_2016` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_30_2022` | point-in-time versions before 2026-07-16 not added: the folder was published before they were read (history is append-only) |
| `pit:l_31_1995` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_31_2001` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_31_2008` | point-in-time versions before 2026-02-10 not added: the folder was published before they were read (history is append-only) |
| `pit:l_31_2011` | point-in-time versions before 2026-04-15 not added: the folder was published before they were read (history is append-only) |
| `pit:l_31_2012` | point-in-time versions before 2026-09-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_31_2014` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_32_1961` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_32_1995` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_32_1998` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_32_2003` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_32_2008` | point-in-time versions before 2025-02-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_32_2018` | point-in-time versions before 2026-06-22 not added: the folder was published before they were read (history is append-only) |
| `pit:l_33_1999` | point-in-time versions before 2026-05-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_33_2005` | point-in-time versions before 2025-06-18 not added: the folder was published before they were read (history is append-only) |
| `pit:l_34_1996` | point-in-time versions before 2026-06-12 not added: the folder was published before they were read (history is append-only) |
| `pit:l_34_1999` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_34_2000` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_35_2007` | point-in-time versions before 2022-01-20 not added: the folder was published before they were read (history is append-only) |
| `pit:l_35_2008` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_35_2012` | point-in-time versions before 2026-04-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_36_2002` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_36_2007` | point-in-time versions before 2025-06-18 not added: the folder was published before they were read (history is append-only) |
| `pit:l_37_1961` | point-in-time versions before 2026-11-07 not added: the folder was published before they were read (history is append-only) |
| `pit:l_37_2007` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_37_2012` | point-in-time versions before 2025-12-05 not added: the folder was published before they were read (history is append-only) |
| `pit:l_37_2014` | point-in-time versions before 2025-02-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_39_1961` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_39_2007` | point-in-time versions before 2019-07-23 not added: the folder was published before they were read (history is append-only) |
| `pit:l_3_1973` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_3_1986` | point-in-time versions before 2026-07-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_3_2005` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_3_2018` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_3_2019` | point-in-time versions before 2026-06-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_40_1961` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_40_2002` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_41_2002` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_41_2014` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_42_1998` | point-in-time versions before 2021-10-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_42_2003` | point-in-time versions before 2026-04-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_42_2014` | point-in-time versions before 2026-07-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_48_2002` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_4_1946` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_4_1971` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_4_1994` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_4_1997` | point-in-time versions before 2026-04-06 not added: the folder was published before they were read (history is append-only) |
| `pit:l_4_1998` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_4_1999` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_4_2008` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_4_2012` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_4_2017` | point-in-time versions before 2019-07-23 not added: the folder was published before they were read (history is append-only) |
| `pit:l_4_2021` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_4_2023` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_50_2002` | point-in-time versions before 2026-04-06 not added: the folder was published before they were read (history is append-only) |
| `pit:l_51_2002` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_5_1934` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_5_1935` | point-in-time versions before 2025-06-18 not added: the folder was published before they were read (history is append-only) |
| `pit:l_5_1947` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_5_1948` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_5_1974` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_5_1998` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_5_1999` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_5_2003` | point-in-time versions before 2026-07-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_5_2011` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_6_1950` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_6_1951` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_6_1967` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_6_1987` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_6_1988` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_6_1997` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_6_1999` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_6_2005` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_6_2011` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_6_2012` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_7_1908` | point-in-time versions before 2021-10-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_7_1949` | point-in-time versions before 2020-03-25 not added: the folder was published before they were read (history is append-only) |
| `pit:l_7_1995` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_7_2005` | point-in-time versions before 2026-07-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_7_2009` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_7_2014` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:l_7_2020` | point-in-time versions before 2026-06-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_7_2025` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_1948` | point-in-time versions before 2026-07-17 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_1977` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_1989` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_1990` | point-in-time versions before 2026-06-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_1998` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_1999` | point-in-time versions before 2025-07-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_2005` | point-in-time versions before 2026-07-16 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_2010` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_2015` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_2018` | point-in-time versions before 2025-02-21 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_2019` | point-in-time versions before 2023-05-30 not added: the folder was published before they were read (history is append-only) |
| `pit:l_8_2021` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_9_1953` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_9_1966` | point-in-time versions before 2023-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:l_9_1995` | point-in-time versions before 2025-06-18 not added: the folder was published before they were read (history is append-only) |
| `pit:l_9_2000` | point-in-time versions before 2024-10-18 not added: the folder was published before they were read (history is append-only) |
| `pit:l_9_2001` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:l_9_2005` | point-in-time versions before 2024-06-14 not added: the folder was published before they were read (history is append-only) |
| `pit:l_9_2007` | point-in-time versions before 2025-09-19 not added: the folder was published before they were read (history is append-only) |
| `pit:l_9_2013` | point-in-time versions before 2022-01-20 not added: the folder was published before they were read (history is append-only) |
| `pit:l_9_2015` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:l_9_2024` | point-in-time versions before 2025-06-14 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_100_2020` | point-in-time versions before 2023-04-12 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_100_2021` | point-in-time versions before 2025-12-25 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_104_2019` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_108_2023` | point-in-time versions before 2026-05-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_113_2021` | point-in-time versions before 2025-07-10 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_114_2018` | point-in-time versions before 2020-05-14 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_118_2022` | point-in-time versions before 2026-04-06 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_119_2018` | point-in-time versions before 2026-07-17 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_11_2017` | point-in-time versions before 2025-12-25 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_11_2021` | point-in-time versions before 2026-10-15 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_125_2021` | point-in-time versions before 2023-08-17 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_128_2018` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_129_2021` | point-in-time versions before 2025-06-27 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_12_2017` | point-in-time versions before 2025-12-25 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_132_2018` | point-in-time versions before 2024-03-28 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_133_2018` | point-in-time versions before 2026-04-21 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_134_2021` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_138_2017` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_138_2020` | point-in-time versions before 2026-06-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_13_2017` | point-in-time versions before 2019-10-10 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_13_2020` | point-in-time versions before 2021-02-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_146_2020` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_147_2020` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_148_2019` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_15_2022` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_184_2020` | point-in-time versions before 2026-06-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_188_2020` | point-in-time versions before 2024-12-16 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_18_2018` | point-in-time versions before 2019-10-15 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_1_2018` | point-in-time versions before 2020-12-31 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_20_2020` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_22_2020` | point-in-time versions before 2026-04-20 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_22_2023` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_24_2017` | point-in-time versions before 2025-12-05 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_24_2018` | point-in-time versions before 2026-04-21 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_2_2024` | point-in-time versions before 2026-04-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_32_2018` | point-in-time versions before 2022-01-20 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_33_2020` | point-in-time versions before 2022-04-29 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_3498` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_36_2022` | point-in-time versions before 2026-06-19 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_37_2022` | point-in-time versions before 2026-06-17 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_3894` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_38_2021` | point-in-time versions before 2024-05-07 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_3943` | point-in-time versions before 2026-04-13 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_4045` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_41_2018` | point-in-time versions before 2024-12-09 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_4204` | point-in-time versions before 2024-02-27 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_4226` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_4253` | point-in-time versions before 2026-04-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_4325` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_4338` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_4387` | point-in-time versions before 2026-04-06 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_44_2018` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_45_2018` | point-in-time versions before 2026-04-06 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_45_2022` | point-in-time versions before 2026-11-16 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_46_2018` | point-in-time versions before 2026-04-06 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_47_2022` | point-in-time versions before 2024-02-26 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5003` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5010` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_50_2020` | point-in-time versions before 2022-04-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_50_2024` | point-in-time versions before 2025-09-03 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5114` | point-in-time versions before 2021-05-17 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5129` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5255` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5593` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5594` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5626` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5651` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5688` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_57_2017` | point-in-time versions before 2023-09-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5956` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5996` | point-in-time versions before 2025-04-14 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_59_2018` | point-in-time versions before 2019-12-23 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_5_2023` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6042` | point-in-time versions before 2026-04-15 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6077` | point-in-time versions before 2026-08-26 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6080` | point-in-time versions before 2020-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6081` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6082` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6083` | point-in-time versions before 2020-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6085` | point-in-time versions before 2019-05-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_60_2019` | point-in-time versions before 2022-04-30 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6107` | point-in-time versions before 2022-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6108` | point-in-time versions before 2026-11-23 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6134` | point-in-time versions before 2020-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6149` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6153` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6229` | point-in-time versions before 2026-06-17 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_64_2023` | point-in-time versions before 2023-11-08 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6597` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6690` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6766` | point-in-time versions before 2021-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6776` | point-in-time versions before 2019-06-27 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_69_2018` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_6_2017` | point-in-time versions before 2022-02-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7016` | point-in-time versions before 2023-09-28 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7028` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_70_2019` | point-in-time versions before 2026-07-08 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7111` | point-in-time versions before 2023-08-09 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_71_2018` | point-in-time versions before 2026-06-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7526` | point-in-time versions before 2019-12-18 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7546` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7676` | point-in-time versions before 2026-03-18 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_76_2018` | point-in-time versions before 2019-05-31 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_77_2025` | point-in-time versions before 2026-06-17 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7816` | point-in-time versions before 2024-01-11 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7833` | point-in-time versions before 2024-12-11 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7838` | point-in-time versions before 2025-08-19 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7938` | point-in-time versions before 2024-06-10 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7954` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7955` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_79_2018` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_7_2019` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8046` | point-in-time versions before 2026-11-23 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_80_2018` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8104` | point-in-time versions before 2026-04-23 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8140` | point-in-time versions before 2025-07-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8162` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8163` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8274` | point-in-time versions before 2026-03-17 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8323` | point-in-time versions before 2020-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8331` | point-in-time versions before 2025-07-31 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8443` | point-in-time versions before 2025-11-24 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8632` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_86_2018` | point-in-time versions before 2026-11-26 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_86_2020` | point-in-time versions before 2025-04-14 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_87_2021` | point-in-time versions before 2026-07-06 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8813` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8916` | point-in-time versions before 2026-06-17 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8974` | point-in-time versions before 2020-01-31 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_89_2019` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_8_2023` | point-in-time versions before 2023-06-30 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_9137` | point-in-time versions before 2025-10-20 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_9138` | point-in-time versions before 2025-12-04 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_9140` | point-in-time versions before 2026-03-17 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_9141` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_91_2019` | point-in-time versions before 2021-09-23 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_9209` | point-in-time versions before 2026-04-14 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_92_2022` | point-in-time versions before 2026-10-02 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_9310` | point-in-time versions before 2021-05-05 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_9313` | point-in-time versions before 2026-08-01 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_9316` | point-in-time versions before 2026-04-22 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_9354` | point-in-time versions before 2023-09-21 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_97_2018` | point-in-time versions before 2020-05-05 not added: the folder was published before they were read (history is append-only) |
| `pit:ro_99_2019` | point-in-time versions before 2026-01-01 not added: the folder was published before they were read (history is append-only) |
| `ro_40_2010` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
| `ro_5717` | no Articles/Regulations/Schedules or no usable "Showing the law from" day |
