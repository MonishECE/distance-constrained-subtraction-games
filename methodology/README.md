# Methodology

Per-theorem verification methodology: each folder pairs the LaTeX method note
(included in the final paper) with the exact script that executes it.

| Folder | Theorem | Script | Certificates |
|---|---|---|---|
| `theorem_A/` | Interval structure and eventual periodicity | Checks run via `theorem_B/verify_theorems_ab.py` (`small_checks`) | None (hand proof + cross-checks) |
| `theorem_B/` | Certified $A=86$ regime, $58\le k\le78$ | `theorem_B/verify_theorems_ab.py` | `data/certificates/theorem_B_audit.{csv,json}`, `data/certificates/full_state_period_certificates_k58_78.csv` |
| `theorem_C/` | Template obstructions + $A=54$ regime, $42\le k\le53$ | `theorem_C/verify_theorem_c.py` | `data/certificates/theorem_C_certificates.csv`, `data/certificates/theorem_C_boundary_counterexamples.csv`, `data/certificates/theorem_C_summary.json` |

Run from the repository root (Python 3.10+, no `-O`; assertions are part of verification):

```console
python methodology/theorem_B/verify_theorems_ab.py
python methodology/theorem_C/verify_theorem_c.py
python src/verify_package.py
```

The methodology scripts import the shared exact solvers from `src/`
(`full_state_analysis.py`: interval recurrence, naive P/N, direct
Sprague--Grundy). The finalized theorem statements live in
`paper/theorems/`; the method notes (`method.tex`) are included in the
final paper's verification-methodology section.
