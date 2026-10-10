# Theorem-by-theorem LaTeX organization

- `main.tex` -- integrated undergraduate-style paper (Theorems A, B, C, methods, conclusion, and works cited).
- `theorem_A/main.tex` -- independently compilable theorem-A manuscript; mathematics proved directly.
- `theorem_B/main.tex` -- independently compilable theorem-B manuscript; exact 21 fixed-k certificates + induction. Uniform symbolic parameter proof **Working on**.
- `theorem_C/main.tex` -- independently compilable theorem-C manuscript; two analytic propositions and 12 fixed-k certificates proved; general regime mechanism **Working on**.
- Each standalone manuscript includes its own typeset **Works cited** section through `shared/works_cited.tex` and therefore contains references in the same PDF.
- `theorem_*/body.tex` -- individual theorem sections used in both their standalone PDFs and the integrated article.
- `shared/preamble.tex`, `shared/works_cited.tex` -- shared formatting and source records.
- `archive/main_initial_2026-10-03.tex` -- historical original, unmodified.
- `archive/main_before_theorem_split_2026-10-09.tex` -- previous Theorems A/B paper, preserved.

## Build from the paper folder

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
(cd theorem_A && pdflatex -interaction=nonstopmode -halt-on-error main.tex)
(cd theorem_B && pdflatex -interaction=nonstopmode -halt-on-error main.tex)
(cd theorem_C && pdflatex -interaction=nonstopmode -halt-on-error main.tex)
```

## Reproduce

```bash
python src/verify_theorems_ab.py
python src/verify_theorem_c.py
python src/affine_region_extractor.py self-test
# Original row_interval_classifier.py is unavailable; see migration/PROVENANCE.md
```

All certificate scripts must be run from the repository root. **No claims that conjectures are proved.**

Compile each entry twice to resolve cross-references. The supplied PDFs predate this consolidation; see migration/VALIDATION_REPORT.md. Single-file equivalents are in overleaf/.
