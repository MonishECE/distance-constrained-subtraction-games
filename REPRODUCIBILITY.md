# Reproducibility

Run from the repository root using Python 3.10+ with assertions enabled (do not use `-O`). Certificate verification uses only the standard library.

```console
python src/verify_package.py
python src/verify_theorems_ab.py
python src/verify_theorem_c.py
python src/verify_hierarchy.py
python src/large_scale_checks.py
python src/targeted_scans.py
python src/distance_subtraction_research.py self-test
python src/affine_region_extractor.py self-test
```

The combined verifier regenerates certificates in a temporary folder, compares them with the published files, and checks manuscript tables. Individual certificate commands update `data/certificates/`. The A/B verifier implements the interval recurrence independently of the direct Boolean and SG cross-checks. The hierarchy verifier certifies the ten regimes (2583 pairs) and falsifies both boundaries of each; `large_scale_checks.py` checks the universal recursion through `n=20000`, the closed-form runs through `n=10^7`, and every regime template through `n=10^7`; `targeted_scans.py` records the negative scans quoted in Theorem C.

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

The original hierarchy has 2,583 certificates. The j=13 extension adds 7,740, for 10,323 pairs across twelve intervals. `python src/check_j13_evidence.py` checks the extension's CSV hash and exact parameter coverage, freshly certifies its endpoints and collapse case, and reproduces adjacent counterexamples. It does not recompute every interior pair. `python src/verify_j13.py` resumes from its JSONL checkpoint; use a fresh copy without `regime_hierarchy_j13_records.jsonl` to recompute every pair (potentially hours).

Finite-window induction extends each certified parameter to all heap sizes. Adjacent failures establish maximal contiguous intervals, not exclusion of disconnected intervals. A certified collapse case does not establish that all other k fail. The `n=10^7` template checks cover endpoints of the ten earlier intervals, not the new j=13 intervals. The uniform regime theorem, upper-endpoint formula, all-group exclusion conjecture, and originality remain open.

After editing canonical files under `paper/`, run `python src/sync_manuscripts.py` to rebuild the main and Theorem C standalone sources; `--check` checks synchronization without writing.
