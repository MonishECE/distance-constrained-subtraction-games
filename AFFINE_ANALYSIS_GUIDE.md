# Exact Python affine-region extractor — instructions and status

## Quick start

```bash
python src/affine_region_extractor.py self-test
python src/affine_region_extractor.py single --k 68 --crosscheck-sg --out results/one_k68
python src/affine_region_extractor.py batch --k-min 58 --k-max 78 --crosscheck-sg --out results/affine
```

The script uses only the Python standard library and the repository's existing `src/full_state_analysis.py`. No regression or floating-point fitting is used.

## What the program does

1. Computes exact Boolean P/N state rows from the recurrence of D(k,1).
2. Checks the full-state k-row periodicity certificate, the starting-residue formula, and optionally the independent SG implementation.
3. Extracts every P-state coordinate (s,n) with 1 <= s <= k and 0 <= n < p(k).
4. Labels 8-neighbor connected components of the unwrapped one-period diagram.
5. Finds all maximal exact line segments of length >= 3 in a set of primitive lattice directions: horizontal, vertical, slopes +/-1, +/-2, +/-3, +/-1/2, +/-1/3.
6. Chooses a greedy covering set of segments and stores every remaining P-state coordinate explicitly; checks zero reconstruction errors.
7. Tracks exact lines across neighboring k values by testing rational affine formulas for invariant, endpoints, and length. A tracked line must match *every predicted field* exactly in each claimed k range.
8. Validates the union of tracked lines against the full P-state sets, reporting false positives and false negatives.
9. Performs finite-prefix counterexample searches for the same starting-position formula at k=56,57,79,80.

## Key outputs

| Output | Purpose |
|---|---|
| `results/affine/ANALYSIS.md` | Readable discovery report with limitations, coverage, tracks, and boundary checks |
| `results/affine/summary.csv` | Per-k exact certificate status, component count, P-state counts, geometric coverage and reconstruction mismatch totals |
| `results/affine/maximal_segments.csv` | Every candidate maximal exact lattice segment |
| `results/affine/selected_regions.csv` | Greedy segment covering set, each with exact equation and endpoints |
| `results/affine/residual_points.csv` | P-state points not explained by selected segments |
| `results/affine/component_sizes.csv` | Sizes of 8-neighbor geometric components |
| `results/affine/exact_affine_tracks.csv` | Exact affine formulas shared across consecutive k |
| `results/affine/track_only_validation.csv` | Test of tracked formulas *alone*, with explicit missing-state counts |
| `results/affine/boundary_falsification.csv` | First observed counterexamples outside the proposed k range |

## Why zero false positives is not yet a theorem

The tracks are discovered and tested on the same 21 k values, not proved algebraically for every allowed k. Moreover the union of tracked lines has **nonzero false negatives**. The complete one-period diagram is exactly reconstructed by selected lines **plus residual points**, which is a verified finite encoding, not a short uniform formula.

A possible next improvement is to group residual points into exact modular intervals or piecewise regions and derive a compact symbolic family covering them all. Then prove no P-to-P legal moves and every N-state has a legal move to P, including the finite transient for k=58..64.

## Cycle caveat

For k=58..64, complete Boolean P/N rows have a transient even though the unrestricted starting-position residues are periodic from n=0. The extractor intentionally analyzes the first start period, so those first-period full-state rows must **not** automatically be treated as the recurring steady-state diagram. A proof-oriented extension should export both the initial and post-transient period and compare their differences.

## Correct research claim

For fixed k values 58..78, the independent recurrence and finite-state certificate confirm the starting-position period and residues for arbitrarily large n via deterministic recurrence. The parameter-dependent line tracks are finite exact observations, not a symbolic proof of a k-interval theorem or a novel infinite family.
