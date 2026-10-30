# How this repository was made (Jersey)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Jersey Law (jerseylaw.je), Jersey Legal Information Board | <https://www.jerseylaw.je/laws/current> | 2026-10-30 | Open States Assembly Licence (OSAL-J) v.1 |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `interpretation` | Interpretation (Jersey) Law 1954 | 6 | 2021-09-28 to 2026-06-19 |
| `proceeds-of-crime` | Proceeds of Crime (Jersey) Law 1999 | 8 | 2021-10-08 to 2025-07-02 |
| `misuse-of-drugs` | Misuse of Drugs (Jersey) Law 1978 | 5 | 2021-09-28 to 2025-12-05 |
| `terrorism` | Terrorism (Jersey) Law 2002 | 2 | 2024-06-14 to 2026-10-02 |
| `police-procedures` | Police Procedures and Criminal Evidence (Jersey) Law 2003 | 5 | 2021-10-01 to 2026-07-17 |
| `companies` | Companies (Jersey) Law 1991 | 6 | 2024-02-27 to 2026-09-30 |
| `employment` | Employment (Jersey) Law 2003 | 3 | 2025-02-21 to 2026-04-17 |
| `criminal-procedure` | Criminal Procedure (Jersey) Law 2018 | 3 | 2023-09-21 to 2026-08-01 |
| `sexual-offences` | Sexual Offences (Jersey) Law 2018 | 2 | 2024-02-27 to 2026-04-06 |
| `human-rights` | Human Rights (Jersey) Law 2000 | 2 | 2021-10-01 to 2024-01-11 |
| `data-protection` | Data Protection (Jersey) Law 2018 | 8 | 2020-11-25 to 2026-10-02 |

The build made 68 commits:

| Commits | Kind |
| ---: | --- |
| 11 | first version of an act |
| 34 | one law on its in-force day |
| 23 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 45 laws in the record.
- 84 tags.

## Dates

Each commit is dated at noon (Europe/Jersey) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Each version is the official consolidated version on jerseylaw.je, dated from the "Showing the law from" day the page states for it (Legislation (Jersey) Law 2021). https://www.jerseylaw.je/laws/current

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `cd087e3b02581d18b4ae0101f13ed22383897c7bdd021eb14ec95d2fe65b111a` (10816869 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

50 versions of 11 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- English is built: Jersey legislation is enacted in English.
- Only official consolidations published at jerseylaw.je/laws/current/ are read: the current page of each Law and earlier copies of that same page.
- Each version is dated from the "Showing the law from" day its page states. The first version of each Law is "oldest version available", credited to the publisher.
- Part, division and cross headings, endnotes, history tables and tables of renumbered provisions are not law text and are left out; footnote markers such as [1] are dropped. Tables inside schedules are not kept as tables.
- Interpretation (Jersey) Law 1954: 6 official consolidations, one per "Showing the law from" day; a changed Article or Schedule is credited to an amending law only where that version's endnotes name the law for it and the version's day is one of the law's commencement days in its Table of Legislation History; otherwise it is left unexplained.
- Proceeds of Crime (Jersey) Law 1999: 8 official consolidations, one per "Showing the law from" day; a changed Article or Schedule is credited to an amending law only where that version's endnotes name the law for it and the version's day is one of the law's commencement days in its Table of Legislation History; otherwise it is left unexplained.
- Misuse of Drugs (Jersey) Law 1978: 5 official consolidations, one per "Showing the law from" day; a changed Article or Schedule is credited to an amending law only where that version's endnotes name the law for it and the version's day is one of the law's commencement days in its Table of Legislation History; otherwise it is left unexplained.
- Terrorism (Jersey) Law 2002: 2 official consolidations, one per "Showing the law from" day; a changed Article or Schedule is credited to an amending law only where that version's endnotes name the law for it and the version's day is one of the law's commencement days in its Table of Legislation History; otherwise it is left unexplained.
- Police Procedures and Criminal Evidence (Jersey) Law 2003: 5 official consolidations, one per "Showing the law from" day; a changed Article or Schedule is credited to an amending law only where that version's endnotes name the law for it and the version's day is one of the law's commencement days in its Table of Legislation History; otherwise it is left unexplained.
- Companies (Jersey) Law 1991: 6 official consolidations, one per "Showing the law from" day; a changed Article or Schedule is credited to an amending law only where that version's endnotes name the law for it and the version's day is one of the law's commencement days in its Table of Legislation History; otherwise it is left unexplained.
- Employment (Jersey) Law 2003: 3 official consolidations, one per "Showing the law from" day; a changed Article or Schedule is credited to an amending law only where that version's endnotes name the law for it and the version's day is one of the law's commencement days in its Table of Legislation History; otherwise it is left unexplained.
- Criminal Procedure (Jersey) Law 2018: 3 official consolidations, one per "Showing the law from" day; a changed Article or Schedule is credited to an amending law only where that version's endnotes name the law for it and the version's day is one of the law's commencement days in its Table of Legislation History; otherwise it is left unexplained.
- Sexual Offences (Jersey) Law 2018: 2 official consolidations, one per "Showing the law from" day; a changed Article or Schedule is credited to an amending law only where that version's endnotes name the law for it and the version's day is one of the law's commencement days in its Table of Legislation History; otherwise it is left unexplained.
- Human Rights (Jersey) Law 2000: 2 official consolidations, one per "Showing the law from" day; a changed Article or Schedule is credited to an amending law only where that version's endnotes name the law for it and the version's day is one of the law's commencement days in its Table of Legislation History; otherwise it is left unexplained.
- Data Protection (Jersey) Law 2018: 8 official consolidations, one per "Showing the law from" day; a changed Article or Schedule is credited to an amending law only where that version's endnotes name the law for it and the version's day is one of the law's commencement days in its Table of Legislation History; otherwise it is left unexplained.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code wrote the scripts and chose the sources; it did not write or alter any legal text. The code runs no model.
