# Reproduce from the repository root

Python 3.10+; no external packages for verification:

```cmd
python src/verify_package.py
python src/verify_theorems_ab.py
python src/verify_theorem_c.py
python src/distance_subtraction_research.py self-test
python src/affine_region_extractor.py self-test
```

The package verifier works in a temporary copy, so it does not modify tracked certificates. Direct certificate commands intentionally regenerate their outputs. Python assertions must be enabled; do not use `-O`.

Compile the integrated paper from `paper`, each standalone from its own theorem folder, twice using `pdflatex -interaction=nonstopmode -halt-on-error main.tex`. The single-file versions in `overleaf` include the bibliography directly and need no BibTeX or image assets.

Optional C++ check: `g++ -std=c++17 -O3 src/distance_subtraction_research.cpp -o scanner.exe` then `scanner.exe self-test`. Plot dependencies are separate from theorem verification. Historical .log files are intentionally tracked even though new LaTeX logs are ignored.

Full exploratory scans are historical evidence; this consolidation does not rerun the N=500,000 scans. Certificates are stronger, deterministic finite premises for the specific infinite-n conclusions.
