# Jersey: law history in git

A first build of the law of Jersey as git: one file per provision, with the official text and its date taken from the official consolidation on [jerseylaw.je](https://www.jerseylaw.je). It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `je/`.

**What is in it now** (language: English, the language of Jersey legislation)

| Folder | Law | Versions | History |
| --- | --- | ---: | --- |
| `interpretation/` | Interpretation (Jersey) Law 1954 | 6 | Official consolidations from 2021-09-28 to 2026-06-19, the last still current |
| `proceeds-of-crime/` | Proceeds of Crime (Jersey) Law 1999 | 8 | Official consolidations from 2021-10-08 to 2025-07-02, the last still current |
| `misuse-of-drugs/` | Misuse of Drugs (Jersey) Law 1978 | 5 | Official consolidations from 2021-09-28 to 2025-12-05, the last still current |
| `terrorism/` | Terrorism (Jersey) Law 2002 | 2 | Official consolidations from 2024-06-14 to 2026-10-02, the last still current |
| `police-procedures/` | Police Procedures and Criminal Evidence (Jersey) Law 2003 | 5 | Official consolidations from 2021-10-01 to 2026-07-17, the last still current |
| `companies/` | Companies (Jersey) Law 1991 | 6 | Official consolidations from 2024-02-27 to 2026-09-30, the last still current |
| `employment/` | Employment (Jersey) Law 2003 | 3 | Official consolidations from 2025-02-21 to 2026-04-17, the last still current |
| `criminal-procedure/` | Criminal Procedure (Jersey) Law 2018 | 3 | Official consolidations from 2023-09-21 to 2026-08-01, the last still current |
| `sexual-offences/` | Sexual Offences (Jersey) Law 2018 | 2 | Official consolidations from 2024-02-27 to 2026-04-06, the last still current |
| `human-rights/` | Human Rights (Jersey) Law 2000 | 2 | Official consolidations from 2021-10-01 to 2024-01-11, the last still current |
| `data-protection/` | Data Protection (Jersey) Law 2018 | 8 | Official consolidations from 2020-11-25 to 2026-10-02, the last still current |

## What it does not show

- **Who made each change.** A changed Article or Schedule is credited to an amending law only when that version's own endnotes name the law for it and the version's date is one of the law's commencement dates in its Table of Legislation History (or the date a Law Revision Board item revised it). Anything else is committed by the publisher as an unexplained change.
- **Coverage.** Jersey has no penal, civil or commercial code; criminal law is customary law plus statutes such as the Sexual Offences, Proceeds of Crime, Misuse of Drugs, Terrorism and Police Procedures and Criminal Evidence Laws included here. Jersey has no single constitutional text, and many more Laws are not yet included.
- **Headings and notes.** Part, division and cross headings, endnotes, the legislation history table and footnote markers are not law text and are not in the files. Tables inside schedules are not kept as tables.

## How it is checked

Every version names its source page and the sha256 of the bytes it was read from. Each version is read back from git and must match `corpus.json` (`tools/check_repo.py`); the results are in `REPRODUCE.md`.

## Sources

| Source | Kind | Past versions | Licence |
| --- | --- | --- | --- |
| [Jersey Law](https://www.jerseylaw.je) | Official legislation (Jersey Legal Information Board) | – | Open States Assembly Licence (OSAL-J) v.1 |

## Licence

Jersey legislation: (c) States Assembly, offered under the Open States Assembly Licence (OSAL-J) v.1. The arrangement, tables, commit messages and tools are by Lexifina, under the terms in `LICENSE`. This repository is not legal advice and not an official publication.
