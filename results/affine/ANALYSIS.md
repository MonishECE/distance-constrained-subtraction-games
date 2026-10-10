# Exact affine-region exploration: k=58..78

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
| 58 | 204 | 412 | 30 | 23 | 94.4 | no |
| 59 | 206 | 420 | 30 | 26 | 93.8 | no |
| 60 | 208 | 422 | 30 | 25 | 94.1 | no |
| 61 | 210 | 426 | 30 | 25 | 94.1 | no |
| 62 | 212 | 432 | 31 | 25 | 94.2 | no |
| 63 | 214 | 439 | 32 | 25 | 94.3 | no |
| 64 | 216 | 448 | 32 | 31 | 93.1 | no |
| 65 | 218 | 452 | 32 | 31 | 93.1 | yes |
| 66 | 220 | 452 | 31 | 31 | 93.1 | yes |
| 67 | 222 | 462 | 33 | 31 | 93.3 | yes |
| 68 | 224 | 462 | 32 | 31 | 93.3 | yes |
| 69 | 226 | 466 | 32 | 31 | 93.3 | yes |
| 70 | 228 | 466 | 33 | 25 | 94.6 | yes |
| 71 | 230 | 470 | 31 | 31 | 93.4 | yes |
| 72 | 232 | 470 | 32 | 25 | 94.7 | yes |
| 73 | 234 | 474 | 32 | 25 | 94.7 | yes |
| 74 | 236 | 471 | 30 | 25 | 94.7 | yes |
| 75 | 238 | 478 | 31 | 27 | 94.4 | yes |
| 76 | 240 | 477 | 29 | 27 | 94.3 | yes |
| 77 | 242 | 481 | 28 | 29 | 94.0 | yes |
| 78 | 244 | 483 | 27 | 29 | 94.0 | yes |

## Exact cross-parameter tracks

30 qualifying contiguous tracks.

- **k=58..78**, direction (1,0), invariant `c=(1)*k+(87)`, `s0=(0)*k+(1)`, `n0=(1)*k+(87)`, `s1=(1)*k+(0)`, `n1=(1)*k+(87)`
- **k=58..78**, direction (1,0), invariant `c=(0)*k+(86)`, `s0=(0)*k+(1)`, `n0=(0)*k+(86)`, `s1=(1)*k+(0)`, `n1=(0)*k+(86)`
- **k=58..78**, direction (1,0), invariant `c=(0)*k+(0)`, `s0=(0)*k+(1)`, `n0=(0)*k+(0)`, `s1=(1)*k+(0)`, `n1=(0)*k+(0)`
- **k=58..78**, direction (1,0), invariant `c=(0)*k+(14)`, `s0=(0)*k+(13)`, `n0=(0)*k+(14)`, `s1=(0)*k+(15)`, `n1=(0)*k+(14)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(85)`, `s0=(0)*k+(41)`, `n0=(0)*k+(126)`, `s1=(1)*k+(0)`, `n1=(1)*k+(85)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(86)`, `s0=(0)*k+(42)`, `n0=(0)*k+(128)`, `s1=(1)*k+(0)`, `n1=(1)*k+(86)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(87)`, `s0=(0)*k+(43)`, `n0=(0)*k+(130)`, `s1=(1)*k+(0)`, `n1=(1)*k+(87)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(-1)`, `s0=(0)*k+(31)`, `n0=(0)*k+(30)`, `s1=(0)*k+(43)`, `n1=(0)*k+(42)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(0)`, `s0=(0)*k+(30)`, `n0=(0)*k+(30)`, `s1=(0)*k+(42)`, `n1=(0)*k+(42)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(1)`, `s0=(0)*k+(29)`, `n0=(0)*k+(30)`, `s1=(0)*k+(41)`, `n1=(0)*k+(42)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(0)`, `s0=(0)*k+(54)`, `n0=(0)*k+(54)`, `s1=(0)*k+(58)`, `n1=(0)*k+(58)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(1)`, `s0=(0)*k+(53)`, `n0=(0)*k+(54)`, `s1=(0)*k+(57)`, `n1=(0)*k+(58)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(-1)`, `s0=(0)*k+(23)`, `n0=(0)*k+(22)`, `s1=(0)*k+(27)`, `n1=(0)*k+(26)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(0)`, `s0=(0)*k+(22)`, `n0=(0)*k+(22)`, `s1=(0)*k+(26)`, `n1=(0)*k+(26)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(1)`, `s0=(0)*k+(21)`, `n0=(0)*k+(22)`, `s1=(0)*k+(25)`, `n1=(0)*k+(26)`
- **k=58..78**, direction (1,1), invariant `c=(1)*k+(86)`, `s0=(1)*k+(-2)`, `n0=(2)*k+(84)`, `s1=(1)*k+(0)`, `n1=(2)*k+(86)`
- **k=58..78**, direction (1,1), invariant `c=(0)*k+(1)`, `s0=(0)*k+(1)`, `n0=(0)*k+(2)`, `s1=(0)*k+(3)`, `n1=(0)*k+(4)`
- **k=58..78**, direction (1,2), invariant `c=(0)*k+(-8)`, `s0=(0)*k+(7)`, `n0=(0)*k+(6)`, `s1=(0)*k+(9)`, `n1=(0)*k+(10)`
- **k=58..78**, direction (2,1), invariant `c=(0)*k+(9)`, `s0=(0)*k+(7)`, `n0=(0)*k+(8)`, `s1=(0)*k+(11)`, `n1=(0)*k+(10)`
- **k=59..78**, direction (1,1), invariant `c=(0)*k+(-1)`, `s0=(0)*k+(55)`, `n0=(0)*k+(54)`, `s1=(0)*k+(59)`, `n1=(0)*k+(58)`
- **k=60..78**, direction (1,1), invariant `c=(0)*k+(87)`, `s0=(0)*k+(1)`, `n0=(0)*k+(88)`, `s1=(0)*k+(3)`, `n1=(0)*k+(90)`
- **k=58..75**, direction (1,1), invariant `c=(1)*k+(88)`, `s0=(0)*k+(1)`, `n0=(1)*k+(89)`, `s1=(0)*k+(3)`, `n1=(1)*k+(91)`
- **k=64..78**, direction (1,2), invariant `c=(0)*k+(78)`, `s0=(0)*k+(7)`, `n0=(0)*k+(92)`, `s1=(0)*k+(9)`, `n1=(0)*k+(96)`
- **k=64..78**, direction (2,1), invariant `c=(0)*k+(181)`, `s0=(0)*k+(7)`, `n0=(0)*k+(94)`, `s1=(0)*k+(11)`, `n1=(0)*k+(96)`
- **k=67..78**, direction (1,0), invariant `c=(0)*k+(100)`, `s0=(0)*k+(13)`, `n0=(0)*k+(100)`, `s1=(0)*k+(15)`, `n1=(0)*k+(100)`

## Track-only classification validation

| k | active tracks | true P-cells | covered by tracks | false positives | false negatives |
|---:|---:|---:|---:|---:|---:|
| 58 | 23 | 412 | 315 | 0 | 97 |
| 59 | 24 | 420 | 326 | 0 | 94 |
| 60 | 25 | 422 | 335 | 0 | 87 |
| 61 | 25 | 426 | 341 | 0 | 85 |
| 62 | 25 | 432 | 347 | 0 | 85 |
| 63 | 25 | 439 | 353 | 0 | 86 |
| 64 | 27 | 448 | 365 | 0 | 83 |
| 65 | 27 | 452 | 371 | 0 | 81 |
| 66 | 26 | 452 | 374 | 0 | 78 |
| 67 | 27 | 462 | 383 | 0 | 79 |
| 68 | 27 | 462 | 389 | 0 | 73 |
| 69 | 27 | 466 | 395 | 0 | 71 |
| 70 | 25 | 466 | 395 | 0 | 71 |
| 71 | 25 | 470 | 401 | 0 | 69 |
| 72 | 25 | 470 | 407 | 0 | 63 |
| 73 | 25 | 474 | 413 | 0 | 61 |
| 74 | 25 | 471 | 419 | 0 | 52 |
| 75 | 27 | 478 | 435 | 0 | 43 |
| 76 | 26 | 477 | 438 | 0 | 39 |
| 77 | 26 | 481 | 444 | 0 | 37 |
| 78 | 26 | 483 | 450 | 0 | 33 |

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
