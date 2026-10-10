# Distance-Constrained Subtraction Games

Research on impartial take-away games in which consecutive removals must differ by more than a fixed distance.

**Authors:** Monish Krishna Bandaru, Rithwik Krishna Gummadi, Santosh Krishna Reddy.

From a heap of size `n`, a move removes `1 ≤ r ≤ min(k,n)` counters. After a previous removal `s`, it must also satisfy `|r−s| > m`. The first move has no previous-removal restriction. A player with no legal move loses.

## Results

| Result | Scope |
|---|---|
| Theorem A | Exact interval structure of losing full-state rows and eventual P/N periodicity for fixed `k ≥ 1, m ≥ 0` |
| Theorem B | For `m=1, k=58..78`, losing starting heaps satisfy `n mod (2k+88) ∈ {0,86,k+87}` |
| Theorem C | Template obstruction and period-collapse results; for `m=1, k=42..53`, losing starts satisfy `n mod (2k+56) ∈ {0,54,k+55}` |

The B/C parameter ranges are proved by exact finite certificates and induction. At `k=53`, the least starting period is `54`, although the displayed modulus is `162`. A uniform symbolic explanation of the regimes and a general parameter hierarchy remain open. A comprehensive originality review is also open.

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

This runs the solver self-tests, verifies both certificate families and boundary counterexamples, and checks the manuscript tables. See [reproducibility instructions](REPRODUCIBILITY.md) for individual commands and C++/LaTeX builds.

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
