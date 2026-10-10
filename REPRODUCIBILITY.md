# Reproducibility

Run from the repository root using Python 3.10+ with assertions enabled (do not use `-O`). Certificate verification uses only the standard library.

```console
python src/verify_package.py
python src/verify_theorems_ab.py
python src/verify_theorem_c.py
python src/distance_subtraction_research.py self-test
python src/affine_region_extractor.py self-test
```

The combined verifier regenerates certificates in a temporary folder, compares them with the published files, and checks manuscript tables. Individual certificate commands update `data/certificates/`. The A/B verifier implements the interval recurrence independently of the direct Boolean and SG cross-checks.

## C++17 scanner

```console
g++ -std=c++17 -O3 src/distance_subtraction_research.cpp -o scanner.exe
scanner.exe self-test
```

On Linux/macOS use `./scanner.exe self-test`. C++ compilation is separate from the Python verification suite.

## Optional figure and affine analysis

```console
python -m pip install -r requirements.txt
python src/full_state_analysis.py plot --k 68 --out figures/full_state_k68_p_positions.png
python src/affine_region_extractor.py batch --k-min 58 --k-max 78 --crosscheck-sg --out results/affine
```

The plotting dependencies are NumPy and Matplotlib. See `AFFINE_ANALYSIS_GUIDE.md` and `results/affine/ANALYSIS.md` for the distinction between exact finite covers and unresolved symbolic classifications.

## LaTeX

From `paper/`, run twice:

```console
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Compile each separate theorem's `main.tex` from its own folder twice. Alternatively, upload one file from `overleaf/` to a blank Overleaf project; those files include all prerequisites and references. The modular paper sources are canonical; regenerate single-file copies after changing them.

## Evidence boundaries

The checks establish 21 fixed-k certificates for B, 12 for C, and eight finite boundary counterexamples. The paper's induction extends the certified finite premises to all heap sizes for those parameters. Tests do not establish the conjectured parameter hierarchy or originality. Supporting deep-scan datasets are retained; the full scans are not rerun by the verification suite.
