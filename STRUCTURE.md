# Structure

| Folder | What it holds |
| --- | --- |
| `laws/<year>/<NN>-<slug>/` | A Law of the States of Jersey, by the year and number of the Law (L.n/yyyy), e.g. `laws/2005/08-states-of-jersey/` (L.8/2005), `laws/1954/17-interpretation/` (L.17/1954) |
| `regulations-and-orders/<year>/<NNN>-<slug>/` | Subordinate legislation (Regulations of the States, Orders of Ministers, Rules of Court), by its R&O year and number, e.g. `regulations-and-orders/2022/036-limited-liability-companies-winding-up-and-dissolution-regulations/` (R&O.36/2022); R&Os from before yearly numbering by their running number, `regulations-and-orders/<year>/ro-NNNN-<slug>/` |
| `orders-in-council/<year>/<NN>-<slug>/` | Orders in Council extending to Jersey, as published on jerseylaw.je |

Each folder holds one file per Article (`art-001.md`), Regulation (`reg-001.md`), Rule (`rule-001.md`) or Schedule
(`sch-01.md`), `long-title.md` where the instrument has one, and a `README.md` listing the provisions. A letter suffix
is an inserted provision (`art-015-a.md` is Article 15A). Part and cross headings, endnotes and history tables are not
law text and are left out. No folder holds more than 1,000 entries. Folder names are in English, the language Jersey
legislation is enacted in; older Laws keep their French titles (`loi-1880-sur-la-propriete-fonciere`).

## Dates

Each version is one commit, dated 12:00 Europe/Jersey on the day it took effect, which its `In-force:` trailer
repeats; `In-force-basis:` says where that day comes from:

- `commencement (Table of Legislation History)`: a Law as enacted, on the one commencement day the Table of
  Legislation History of its own current consolidation gives it (Laws brought into force in stages get no as-enacted
  version);
- `Showing the law from (official consolidation)`: the current consolidation, on the "Showing the law from" day the
  page states. When exactly one law in the Table commenced that day, the commit is credited to it; otherwise to the
  publisher.

Before 1970 git cannot store a date: such commits are dated 1 January 1970 (a second apart, in order) and carry the
real day in the subject and the `In-force:` trailer. No date in this repository is the day we downloaded anything.
