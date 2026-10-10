# Theorem C finite audit and limitations

**Date:** 2026-10-09. **Status:** Theorem C as an unrestricted hierarchy remains **Working on**. All claimed subresults are stated with precise evidence.

## Verified and proved

- Analytic necessary condition `k<A` for an A-template to hold: remove all A stones on the first turn if `k>=A`.
- Abstract three-residue period collapse iff `k=A-1`: group translation argument, independent of any computation.
- Fixed-k `A=54` template for each `k=42..53`: 12 exact finite-window certificates, full recursion verified and independently cross-checked using direct SG. Starting least period `2*k+56` for `k=42..52`, period `54` for `k=53`.
- Eight direct P/N-verified counterexamples to unqualified formula extension: see `data/certificates/theorem_C_boundary_counterexamples.csv`.
- Previous Theorem B: 21 fixed-k exact certificates for `k=58..78`; no uniform symbolic proof.

## Process

1. Inspected `paper/main.tex` and audit artifacts from the preceding formal A/B release.
2. Used interval recurrence to search for complete k-row repetition witnesses for the A=54 formula.
3. Independently checked every full-state P-row and starting P flag through each required bridge bound against direct Sprague-Grundy calculations.
4. Applied the formal induction lemmas from Theorem B to extend fixed-k certificates to all heap sizes n.
5. Proved a first-move necessary condition and arithmetic coset lemma analytically; tested boundary cases with a naive P/N recurrence.
6. Audited cited mathematical sources and separated external context from original proof work.
7. Compiled the integrated paper and three standalone theorem PDFs.

## Reproduction

From the nested project root:

```sh
python src/verify_theorems_ab.py
python src/verify_theorem_c.py
python src/affine_region_extractor.py self-test
python src/row_interval_classifier.py self-test
cd paper && pdflatex -interaction=nonstopmode -halt-on-error main.tex
cd theorem_A && pdflatex -interaction=nonstopmode -halt-on-error main.tex
cd ../theorem_B && pdflatex -interaction=nonstopmode -halt-on-error main.tex
cd ../theorem_C && pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Unproved / Working on

- Why the constants A=54 and A=86 arise from a parameter-uniform construction.
- Exact symbolic derivation of the endpoint k=78 for A=86.
- A closed piecewise full-state formula `Q_n` for every k in a regime.
- Any infinite hierarchy of A-values.
- Exhaustive literature priority/originality review.

All of the above are explicitly **Working on** in the separate manuscripts.
