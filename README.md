# Distance-Constrained Subtraction Games

Clean research snapshot assembled October 10, 2026 from both remote branches and the historical affine ZIP. Import **this folder's contents** at the repository root; do not create another nested repository folder.

## Research status

- Theorem A: interval row structure and eventual P/N periodicity, proved from the recurrence.
- Theorem B: 21 fixed parameters k=58..78, exact computer-assisted certificates plus induction; least start period 2k+88.
- Theorem C: analytic template obstruction and period collapse; 12 fixed parameters k=42..53 with modulus 2k+56. At k=53 the least start period is 54.
- A uniform symbolic regime classification and infinite hierarchy remain open. No originality claim has been established.

## Start here

Run `python src/verify_package.py` from this folder (Python 3.10+; certificate checks need no third-party packages). Read `migration/WINDOWS_CMD.md` before replacing a checkout, and review `migration/DELETION_AUDIT.csv`.

| Folder | Purpose |
|---|---|
| paper/ | Integrated and separate A/B/C LaTeX, citations, supplied PDFs |
| overleaf/ | Single-file integrated and A/B/C sources; upload one .tex as main.tex |
| src/ | Original Python/C++ engines, recovered affine extractor, rebuilt A/B verifier, C verifier |
| data/certificates/ | Regenerated exact certificates and boundary failures |
| data/, reports/, figures/, results/ | Preserved scans, evidence and affine extraction outputs |
| docs/, literature/, logs/ | Methodology, literature leads and historical logs |
| archive/ | Original drafts, superseded documents and complete Git history bundle |
| migration/ | Pinned branch inventory, file audit, safe replacement tool and validation report |

The A/B verifier is newly reconstructed for this consolidation, not recovered original code. The row-interval classifier and its outputs were never present in accessible Git history; no replacement is passed off as the original. See `migration/PROVENANCE.md`.

Optional plots: `python -m pip install -r requirements.txt`. C++: compile with C++17 and run its `self-test`. PDFs are preserved upstream binaries; current compilation status is recorded in the validation report.
