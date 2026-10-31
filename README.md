# Distance-Constrained Subtraction Games

Research on impartial take-away games in which consecutive removals must differ by more than a fixed distance.

**Authors:** Monish Krishna Bandaru, Rithwik Krishna Gummadi, Santosh Krishna Reddy.

From a heap of size `n`, a move removes `1 ≤ r ≤ min(k,n)` counters. After a previous removal `s`, it must also satisfy `|r−s| > m`. The first move has no previous-removal restriction. A player with no legal move loses.

## Results

| Result | Scope |
|---|---|
| Theorem A | Exact interval structure of losing full-state rows and eventual P/N periodicity for fixed `k ≥ 1, m ≥ 0` |
| Theorem B | For `m=1, k=58..78`, losing starting heaps satisfy `n mod (2k+88) ∈ {0,86,k+87}` |
| Theorem C | Universal row recurrence and closed-form run hierarchy; twelve certified parameter intervals through `j=13` (`A=14..21846`), covering 10,323 pairs; template obstructions and certified collapse cases |

The B/C parameter intervals are proved by exact finite certificates and induction. The j=13 extension adds `A=13654, k=10922..13653` and `A=21846, k=15018..20025` (7,740 pairs), plus the certified collapse `A=30038, k=30037`. Its new upper deficit is `d_13=1821`; the adjacent failure at `k=20026` occurs at `n=83746`. The separate checks through `n=10^7` cover endpoints of the ten earlier intervals. Adjacent failures establish maximal contiguous intervals, not exclusion of all other parameters. The uniform regime theorem, upper-endpoint formula, and comprehensive originality review remain open.

## Read the paper

- [Integrated manuscript](paper/main.tex)
- [Theorem A](paper/theorem_A/main.tex), [Theorem B](paper/theorem_B/main.tex), [Theorem C](paper/theorem_C/main.tex)
- [Single-file Overleaf manuscript](overleaf/main.tex)
- [References](paper/references.bib)

Upload `overleaf/main.tex` to a blank Overleaf project and use pdfLaTeX. The separate `overleaf/theorem_*.tex` files are also self-contained.

## Verify the results

Python 3.10+; no external packages are needed for theorem verification:

```console
python src/verify_package.py
```

This runs the solver self-tests, verifies both certificate families and boundary counterexamples, and checks the manuscript tables. Additional checks:

```console
python src/verify_hierarchy.py       # 2583 hierarchy certificates + boundaries
python src/check_j13_evidence.py     # fast artifact audit + fresh endpoint/boundary checks
python src/verify_j13.py             # resumable j=13 run; skips checkpointed records
python src/sync_manuscripts.py --check
python src/large_scale_checks.py     # universal recursion, closed-form runs, n=10^7
```

See [reproducibility instructions](REPRODUCIBILITY.md) for individual commands and C++/LaTeX builds.

## Repository contents

| Directory | Contents |
|---|---|
| `paper/`, `overleaf/` | Manuscripts and bibliography |
| `src/` | Python and C++ solvers, theorem verifiers, affine extractor |
| `data/certificates/` | Exact certificate tables and boundary counterexamples |
| `data/` | Supporting scan datasets |
| `results/affine/` | Exact affine extraction outputs and limitations |
| `figures/` | Representative full-state plot |

Exploratory scan patterns and affine catalogs are computational evidence; they do not establish a uniform symbolic theorem. The theorem verifiers use finite repeated-state windows with an explicitly checked starting-position bridge.
