# Distance-Constrained Dynamic Subtraction Games

Computational research repository for the game family (D(k,m)).

## Research question

How does imposing a minimum separation between consecutive move sizes
change the periodic structure of losing positions in a dynamic
subtraction game?

The current main case is (m=1). A state is ((n,s)), where (n) is the
heap size and (s) is the previous move. A legal removal (r) satisfies

\[
1`\le `{=tex}r`\le `{=tex}`\min`{=tex}(k,n),`\qquad `{=tex}\|r-s\|\>m.
\]

The current proof-oriented question is whether the observed affine
families of periods and starting P-position residues can be derived from
an exact symbolic classification of the full P-state geometry.

## Current status

The repository contains three independent computational layers:

1.  `src/distance_subtraction_research.py` --- original Python SG
    research engine.
2.  `src/distance_subtraction_research.cpp` --- optimized C++17 SG
    scanner used for deep scans.
3.  `src/full_state_analysis.py` --- independent Boolean P/N solver,
    direct SG cross-check, and finite-state period-certificate
    generator.

The strongest current finite-range result is the computer-assisted
certification for every integer (58`\le `{=tex}k`\le78`{=tex}):

\[ p(k)=2k+88, `\qquad`{=tex}
P\_{`\mathrm{start}`{=tex}}`\equiv`{=tex}{0,86,k+87}`\pmod{2k+88}`{=tex}.
\]

For each of these 21 fixed (k)-values, the Boolean recurrence finds two
identical (k)-row full-state windows separated by (p). Since the
recurrence has memory at most (k), equality of these windows forces all
subsequent P/N rows to repeat. The starting-position residue formula is
then checked over the finite prefix required to connect to the certified
cycle.

This is an exact computer-assisted finite-range certification, not yet a
symbolic proof explaining the whole interval simultaneously.

## Repository layout

``` text
distance-subtraction-research/
├── README.md
├── DISCOVERIES.md
├── REPRODUCIBILITY.md
├── GITHUB_PUSH_INSTRUCTIONS.md
├── CHANGELOG.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── distance_subtraction_research.py
│   ├── distance_subtraction_research.cpp
│   └── full_state_analysis.py
├── data/
│   ├── deep_scan/
│   ├── comparison/
│   └── certificates/
├── docs/
│   ├── distance_subtraction_methodology.md
│   └── archive/
├── paper/
│   └── main.tex
├── figures/
│   └── full_state_k68_p_positions.png
├── literature/
│   └── literature_search_terms.txt
├── logs/
└── archive/
```

## Reproduce the certificate table

From the repository root:

``` bash
python src/full_state_analysis.py certificates \
  --k-min 58 --k-max 78 \
  --out data/certificates/full_state_period_certificates_k58_78.csv
```

The script independently cross-checks the Boolean P/N states against a
direct Sprague-Grundy implementation over the finite range needed for
the certificate.

## Reproduce the representative full-state figure

Install the optional plotting dependencies:

``` bash
python -m pip install -r requirements.txt
```

Then run:

``` bash
python src/full_state_analysis.py plot \
  --k 68 \
  --out figures/full_state_k68_p_positions.png
```

For (k=68), the certified period is (224), and the starting P-position
residues are

\[ {0,86,155}`\pmod{224}`{=tex}. \]

## Compile the C++ research scanner

A C++17 compiler is required:

``` bash
g++ -std=c++17 -O3 -DNDEBUG src/distance_subtraction_research.cpp -o distance_subtraction_research
./distance_subtraction_research self-test
```

The `-std=c++17` flag is required because the program uses C++17
facilities including `std::optional`, `std::filesystem`, structured
bindings, and `std::gcd`.

## Deep-scan data

The principal deep scan used

\[
m=1,`\qquad 35`{=tex}`\le `{=tex}k`\le120`{=tex},`\qquad `{=tex}N=500{,}000.
\]

The merged output is stored at:

`data/deep_scan/m1_deep_35_120.csv`

The two major observed affine regimes are:

\[ 42`\le `{=tex}k`\le52`{=tex}: `\quad`{=tex} p=2k+56,`\qquad`{=tex}
P\_{`\mathrm{start}`{=tex}}`\equiv`{=tex}{0,54,k+55}, \]

and

\[ 58`\le `{=tex}k`\le78`{=tex}: `\quad`{=tex} p=2k+88,`\qquad`{=tex}
P\_{`\mathrm{start}`{=tex}}`\equiv`{=tex}{0,86,k+87}. \]

See `DISCOVERIES.md` for the distinction among observed patterns, exact
computer-assisted certificates, and unproved symbolic conjectures.

## Next research phase

The next script should perform exact affine-region extraction on full
P-state coordinates ((n,s)), not least-squares regression. It should
identify exact line/region invariants such as (n-s=C), (n-2s=C), and
their domains, track those components across
(58`\le `{=tex}k`\le78`{=tex}), and produce a candidate symbolic
decomposition

\[
`\mathcal `{=tex}P_k=R_1(k)`\cup`{=tex}`\cdots`{=tex}`\cup `{=tex}R_q(k).
\]

That classification can then be attacked with the standard two-condition
P/N proof: no legal P-to-P move, and every N-state has a legal move to
P.

## Notes

`docs/archive/AI Algorithm & Correctness Proof.docx` is retained as a
historical/supporting draft. It is not the canonical algorithm
description: its statement that a Boolean `isWinning` routine computes
full Grundy values needs correction. The canonical computational
methodology is `docs/distance_subtraction_methodology.md` together with
the source code.

Older scan reports and logs are preserved for auditability, including
the shorter-run (k=80) false-tail episode. The later (N=500{,}000) scan
corrected that interpretation to candidate preperiod (0), period (947).

## NEW — Exact affine-region extraction (Python)

Run from the repository root:

```bash
python src/affine_region_extractor.py self-test
python src/affine_region_extractor.py batch --k-min 58 --k-max 78 --crosscheck-sg --out results/affine
```

Read `AFFINE_ANALYSIS_GUIDE.md` and `results/affine/ANALYSIS.md`. The extractor identifies and tracks exact lattice-line segments, exports all residual P-state points, cross-checks the finite-state certificates and SG values, validates the tracked formulas and reports counterexamples just outside the proposed regime.

**Status:** exact computational region mining, not a finished symbolic proof. The cross-k tracked lines cover a substantial subset of the P-states, with **zero false positives but nonzero false negatives**. The region set plus residual points reconstructs every tested first-period P-state exactly.
