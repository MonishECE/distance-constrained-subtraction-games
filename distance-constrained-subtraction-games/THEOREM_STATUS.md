# Theorem inventory and status (2026-10-09)

| Result | Status | Scope | Evidence |
|---|---|---|---|
| A: exact interval classification | **PROVED** | all fixed k>=1, m>=0, all n | self-contained argument from game recurrence |
| A: eventual full-state and starting P/N periodicity | **PROVED** | all fixed k>=1, m>=0 | finite-window pigeonhole argument |
| B: affine starting outcomes p=2k+88 | **PROVED (computer-assisted fixed k)** | 58<=k<=78 (21 integers), all n | 21 exact k-row certificates + induction, independent SG check |
| B: single symbolic formula yielding regime | **WORKING ON** | parameter-level | missing uniform full-state row formula |
| C: k<A necessary for a valid A-template | **PROVED** | any positive k,A | direct first-move contradiction |
| C: period-collapse iff k=A-1 | **PROVED** | abstract residue template | cyclic-translation orbit proof |
| C: p=2k+56 starting formula | **PROVED (computer-assisted fixed k)** | 42<=k<=53 (12 integers), all n | 12 exact window certificates + induction, independent SG |
| C: explicit neighboring counterexamples | **PROVED (finite counterexamples)** | specified k=41,54..57,79,80 | direct P/N verification |
| C: general hierarchy and symbolic boundaries | **WORKING ON** | arbitrary k,A | no uniform proof or analytic derivation of 54, 86, 78 |

See `paper/main.tex`, the three `paper/theorem_*/` folders, and `paper/WORKS_CITED.md`. The terms **Working on** are intentional and indicate missing proofs, not tentative confidence in a theorem.
