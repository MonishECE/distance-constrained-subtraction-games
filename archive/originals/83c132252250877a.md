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
