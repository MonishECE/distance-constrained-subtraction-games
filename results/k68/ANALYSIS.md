# Exact affine-region exploration: k=68..68

All equations here are **exact descriptions of computed P-state points** inside the *first* starting period `0 <= n < p(k)`. They are not yet symbolic theorems for every k or a complete human proof.

## Methods

- Generate Boolean P-state coordinates from an independent exact recurrence.
- Verify k-row cycle equality and starting residues via a finite-state certificate.
- Independently check SG P/N output when `--crosscheck-sg` is selected.
- Extract all maximal consecutive segments with primitive integer directions and exact invariant `ds*n - dn*s = c`.
- Build a greedy exact line cover; store uncovered points explicitly.
- Reconstruct each first-period P set from selected lines + residual points and count false positives/negatives exhaustively.
- Match segments across k using exact rational affine formulas for invariant, endpoints, and length; report only contiguous exact matches.

## Summary

| k | p | P cells | lines | residual | covered % | full-state period from 0 |
|---:|---:|---:|---:|---:|---:|:---:|
| 68 | 224 | 462 | 32 | 31 | 93.3 | yes |

## Exact cross-parameter tracks

0 qualifying contiguous tracks.


## Track-only classification validation

| k | active tracks | true P-cells | covered by tracks | false positives | false negatives |
|---:|---:|---:|---:|---:|---:|
| 68 | 0 | 462 | 0 | 0 | 462 |

**Meaning:** Tracked affine families alone are not yet a full symbolic classification unless **both** mismatch counts are zero. The per-k exact cover including residual points is checked separately.

## Boundary falsification

| k outside | candidate p | checked through | mismatch count | first mismatch |
|---:|---:|---:|---:|---:|
| 56 | 200 | 600 | 17 | 57 |
| 57 | 202 | 606 | 11 | 58 |
| 79 | 246 | 738 | 5 | 492 |
| 80 | 248 | 744 | 10 | 167 |

## Crucial limitations

A region catalog fit on each k does not prove parameter-wide correctness. The greedy cover is not unique, and connected components can include overlapping lines or nonlinear boundaries. The region catalog plus residual points is an **exact finite description** of each analyzed first period, not automatically a compact uniform symbolic family. Full-state periodicity for k=58..64 starts only after a transient: the first period of full state need not reproduce exactly. No claim is made about k outside the certified 58..78 range.
