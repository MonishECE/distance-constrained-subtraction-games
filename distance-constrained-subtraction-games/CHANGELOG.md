## 2026-10-09 — Theorems A/B formalization and historical paper revision

- Verified oldest `paper/main.tex` Git blob and preserved it unmodified in `paper/archive/`.
- Added self-contained proofs for the interval structure theorem and eventual full-state periodicity.
- Added a new independent Python certificate verifier for 21 exact fixed-parameter affine cases, plus naive and direct SG cross-checks.
- Corrected the finite-prefix metadata to `t+k+p-1` (periods and cycle starts unchanged).
- Wrote a new undergraduate-level paper, bibliography, separate work cited file, proof audit, and process/conclusion record.
- Theorem B is labeled a **computer-assisted finite-range result**, not a uniform symbolic proof; unresolved mathematical questions documented.
- GitHub write was blocked with HTTP 403; no push has been claimed.

# Changelog

## 2026-10-03 --- Repository consolidation

-   Consolidated the Python and C++ research engines, deep-scan outputs,
    methodology, Overleaf source, certificate data, full-state figure,
    literature-search terms, and historical run logs.
-   Added `src/full_state_analysis.py`, an independent Boolean P/N
    solver and finite-state certificate generator with direct SG
    cross-checking.
-   Preserved the (N=500{,}000), (35`\le `{=tex}k`\le120`{=tex}), (m=1)
    merged deep scan.
-   Recorded the two main observed affine regimes:
    -   (42`\le `{=tex}k`\le52`{=tex}): (p=2k+56), residues
        ({0,54,k+55}).
    -   (58`\le `{=tex}k`\le78`{=tex}): (p=2k+88), residues
        ({0,86,k+87}).
-   Recorded exact finite-state computer-assisted certification of the
    second regime for each fixed (k=58,`\ldots`{=tex},78).
-   Corrected the certificate CSV metadata field
    `finite_prefix_check_through_n` to the stronger verification bound
    (t+k+p-1). This does not change cycle starts, periods, residue sets,
    or independent SG cross-check results.
-   Retained older exploratory reports and compiler/runtime logs for
    auditability.

## 2026-10-09 — Exact affine-region Python pipeline

- Added `src/affine_region_extractor.py` with Boolean P-state generation, exact line extraction, 8-neighbor components, greedy line cover, exact rational cross-k tracks, cycle and SG verification, and exhaustive mismatch tests.
- Generated `results/affine/` outputs for every k=58..78 (independent SG cross-checks enabled).
- Identified 30 exact cross-parameter tracks under the extraction/matching conventions. These are empirically verified line families, not yet a complete symbolic theorem.
- Track-only classification has zero false positives but nonzero false negatives; the per-k line cover plus explicitly retained residual points exactly reproduces all tested P-states.
- Added out-of-regime finite-prefix falsification for k=56,57,79,80.


## 2026-10-09 — Exact row intervals and cross-parameter block mining

- Added `src/row_interval_classifier.py`: derives per-row P-state intervals from winning move sets `A_n`; mines exact affine/parity endpoint runs and tracks recurring blocks across `k`.
- Added `results/row_intervals/`: all P-row intervals, piecewise endpoint blocks, cross-k block tracks, summary and analysis.
- Verified the resulting finite classification for `k=58..78` with zero mismatches and independent SG cross-checks.
- Separately documented the general interval lemma and the still-unproved symbolic parameter classification.

## 2026-10-09 — Theorem A/B/C split, cited sources, and Theorem C partial proof
- Kept the oldest historical paper and archived the immediately previous A/B draft.
- Added standalone LaTeX manuscripts in `paper/theorem_A/`, `paper/theorem_B/`, and `paper/theorem_C/`, plus integrated updated `paper/main.tex`.
- Added Theorem C exact 12-parameter certificate verifier and eight boundary falsifications.
- Proved universal necessary template condition `k<A` and arithmetic collapse iff `k=A-1`.
- Added source audit and cite-in-every-manuscript bibliography; marked all incomplete symbolic or general conclusions **Working on**.
