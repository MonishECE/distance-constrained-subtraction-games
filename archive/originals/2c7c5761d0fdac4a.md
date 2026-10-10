# Research update: formal Theorems A/B and paper revision

**Date:** 2026-10-09  
**Based on:** The earliest tracked `paper/main.tex` (Git commit `7fd277c67f6e84e8531e689e5b3a81562106a32b`, dated 2026-10-04) and the latest packaged row-interval research outputs.  
**Repository:** https://github.com/MonishECE/distance-constrained-subtraction-games

## What was done, chronologically

1. **Inspected repository history.** Confirmed the oldest paper version matches the active `paper/main.tex` at the initial source history, and saved that file unchanged under `paper/archive/` to preserve provenance.
2. **Reviewed the previous mathematical and computational claims.** Correctly separated ordinary finite-tail scans, deterministic finite-window certificates, and full symbolic parameter proofs.
3. **Formalized the game and P/N states.** Defined the legal moves, losing-state rows `Q_n`, potential P-reaching move sets `A_n`, and unrestricted-start outcomes.
4. **Proved Theorem A1.** Intersecting the forbidden `s` intervals for each P-reaching move shows every row is an interval; its length is at most `2m+1` except for all-full rows.
5. **Proved Theorem A2.** A fixed `k` gives a deterministic finite-memory row recurrence. Finite windows imply eventual periodicity for the full-state and starting-outcome sequences.
6. **Audited Theorem B.** Wrote a separate Python program implementing Theorem A's interval recurrence and an independent naive Boolean solver. It verifies 36 small parameters and uses an existing SG implementation as a further independent cross-check.
7. **Certified the 21 affine instances.** For each `k=58..78`, found two equal full-state `k`-row windows at distance `2k+88`, verified the starting residue formula over a sufficient prefix, and checked the least period.
8. **Corrected a metadata error.** The old paper's printed finite-prefix numbers were too short; the mathematically required bound is `t+k+p-1`. Corrected data lives in `data/certificates/theorem_B_audit.csv` and the paper's generated certificate table.
9. **Revised the undergraduate research paper.** Updated `paper/main.tex` with an abstract, formal definitions, detailed proofs, certificate method, a table of all 21 cases, figure, limitations, future work, and conclusion. The original paper is archived.
10. **Separated the references.** Added `paper/WORKS_CITED.md`, `paper/references.tex`, and `paper/references.bib` with explicit credit for standard impartial game theory and prior repetition-free game work.
11. **Recorded proof limitations.** A uniform symbolic full-state classification, a structural explanation for the parameter boundaries, and a comprehensive novelty review remain open.

## Result

**Theorem A: fully formalized and proved for every fixed `k>=1, m>=0`** (both exact row structure and eventual periodicity).

**Theorem B: a reproducible computer-assisted theorem for each of the 21 fixed integers `58<=k<=78`**, yielding the unrestricted starting P-position residues `{0,86,k+87}` modulo `2k+88` for all nonnegative heap sizes. This is not yet a parameter-uniform symbolic proof.

## Remaining work toward a master theorem

1. Extract compact piecewise formulas for every P-state row, rather than retaining exceptional rows individually.
2. Substitute the candidate formula into the exact interval recurrence and reduce verification to symbolic interval inequalities.
3. Explain analytically why the recurrence changes at `k=57/58` and `k=78/79`.
4. Transfer the strategy to the second affine block `k=42..52` and test whether a higher-level theorem in the intercept `A` exists.
5. Complete an independent literature review and final student-authored proof audit.

## Repository status

A GitHub connector read succeeded, but branch creation failed with HTTP 403 (`Resource not accessible by integration`). Therefore **these changes have not been pushed to the remote repository**. The prepared ZIP includes all the updated sources and evidence. This statement must be changed only after a confirmed remote commit.
