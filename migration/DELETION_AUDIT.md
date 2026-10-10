# Proposed cleanup audit

No remote files were deleted. Every current branch-head file appears below and in DELETION_AUDIT.csv with a full SHA-256. Original content is preserved byte-for-byte. A migrated checkout has the new root contents; the old nested paths disappear from the new commit.

## main

60 tracked paths audited.

| Old path | Proposed action | Original content retained at |
|---|---|---|
| `.gitignore` | replace_at_same_path | `archive/originals/2d7eae050367577a` |
| `AFFINE_ANALYSIS_GUIDE.md` | retain_same_path | `AFFINE_ANALYSIS_GUIDE.md` |
| `CHANGELOG.md` | replace_at_same_path | `archive/originals/a26d0e95e854f8a5.md` |
| `DISCOVERIES.md` | replace_at_same_path | `archive/originals/4d6e8962d82df54b.md` |
| `GITHUB_PUSH_INSTRUCTIONS.md` | replace_at_same_path | `archive/originals/b1034de08498e718.md` |
| `GITHUB_UPDATE_INSTRUCTIONS.md` | replace_at_same_path | `archive/originals/b0c86be564679dae.md` |
| `MANIFEST_SHA256.txt` | replace_at_same_path | `archive/originals/2d6019d32c13059f.txt` |
| `README.md` | replace_at_same_path | `archive/originals/a5f9aa342ef35f7e.md` |
| `REPRODUCIBILITY.md` | replace_at_same_path | `archive/originals/9a34fdd6f73c69c4.md` |
| `RESEARCH_UPDATE_CONCLUSION.md` | replace_at_same_path | `archive/originals/2c7c5761d0fdac4a.md` |
| `distance-constrained-subtraction-games/.gitignore` | remove_old_path_preserve_content | `archive/originals/2d7eae050367577a` |
| `distance-constrained-subtraction-games/CHANGELOG.md` | remove_old_path_preserve_content | `archive/originals/83c132252250877a.md` |
| `distance-constrained-subtraction-games/DISCOVERIES.md` | remove_old_path_preserve_content | `archive/originals/77afedd6503d2e6a.md` |
| `distance-constrained-subtraction-games/GITHUB_PUSH_INSTRUCTIONS.md` | remove_old_path_preserve_content | `archive/originals/b1034de08498e718.md` |
| `distance-constrained-subtraction-games/MANIFEST_SHA256.txt` | remove_old_path_preserve_content | `archive/originals/2394ea2738d0f15b.txt` |
| `distance-constrained-subtraction-games/README.md` | remove_old_path_preserve_content | `archive/originals/b24886e7a6ee1043.md` |
| `distance-constrained-subtraction-games/REPRODUCIBILITY.md` | remove_old_path_preserve_content | `archive/originals/9a34fdd6f73c69c4.md` |
| `distance-constrained-subtraction-games/archive/bash_test_results/literature_search_terms.txt` | remove_old_path_preserve_content | `archive/originals/a2522c66cc5411f6.txt` |
| `distance-constrained-subtraction-games/archive/bash_test_results/research_report.md` | remove_old_path_preserve_content | `archive/originals/b524298c15935238.md` |
| `distance-constrained-subtraction-games/archive/bash_test_results/scan_results.csv` | remove_old_path_preserve_content | `archive/originals/2496b9f781d7d3da.csv` |
| `distance-constrained-subtraction-games/archive/cpp_test_scan/literature_search_terms.txt` | remove_old_path_preserve_content | `archive/originals/a2522c66cc5411f6.txt` |
| `distance-constrained-subtraction-games/archive/cpp_test_scan/research_report.md` | remove_old_path_preserve_content | `archive/originals/d97db7385c2471b8.md` |
| `distance-constrained-subtraction-games/archive/cpp_test_scan/scan_results.csv` | remove_old_path_preserve_content | `archive/originals/5f05985fcad9fb26.csv` |
| `distance-constrained-subtraction-games/data/certificates/full_state_period_certificates_k58_78.csv` | remove_old_path_preserve_content | `archive/originals/e2a338f463b4e391.csv` |
| `distance-constrained-subtraction-games/data/comparison/m0_m1_m2_k2_15_n10000_scan_results.csv` | remove_old_path_preserve_content | `archive/originals/2496b9f781d7d3da.csv` |
| `distance-constrained-subtraction-games/data/deep_scan/m1_35_80_scan_results.csv` | remove_old_path_preserve_content | `archive/originals/b99f57a2310ee099.csv` |
| `distance-constrained-subtraction-games/data/deep_scan/m1_81_120_scan_results.csv` | remove_old_path_preserve_content | `archive/originals/69500adf45029e43.csv` |
| `distance-constrained-subtraction-games/data/deep_scan/m1_deep_35_120.csv` | remove_old_path_preserve_content | `archive/originals/3df2c5f54d3139bd.csv` |
| `distance-constrained-subtraction-games/data/exploratory/m1_k5_100_n200000_scan_results.csv` | remove_old_path_preserve_content | `archive/originals/d301182c59539053.csv` |
| `distance-constrained-subtraction-games/docs/archive/AI Algorithm & Correctness Proof.docx` | remove_old_path_preserve_content | `docs/archive/AI Algorithm & Correctness Proof.docx` |
| `distance-constrained-subtraction-games/docs/distance_subtraction_methodology.md` | remove_old_path_preserve_content | `archive/originals/149e469cbe1e3b2d.md` |
| `distance-constrained-subtraction-games/figures/full_state_k68_p_positions.png` | remove_old_path_preserve_content | `figures/full_state_k68_p_positions.png` |
| `distance-constrained-subtraction-games/literature/literature_search_terms.txt` | remove_old_path_preserve_content | `archive/originals/a2522c66cc5411f6.txt` |
| `distance-constrained-subtraction-games/logs/compiler_error_missing_cpp17.md` | remove_old_path_preserve_content | `archive/originals/b4d44664ada81e25.md` |
| `distance-constrained-subtraction-games/paper/main.tex` | remove_old_path_preserve_content | `archive/originals/69944f5008592be0.tex` |
| `distance-constrained-subtraction-games/reports/m1_deep_35_80_report.md` | remove_old_path_preserve_content | `archive/originals/455192afd052c73d.md` |
| `distance-constrained-subtraction-games/reports/m1_deep_81_120_report.md` | remove_old_path_preserve_content | `archive/originals/de34d781dde9619d.md` |
| `distance-constrained-subtraction-games/reports/m1_k5_100_n200000_report.md` | remove_old_path_preserve_content | `archive/originals/a8d653a7803bf198.md` |
| `distance-constrained-subtraction-games/requirements.txt` | remove_old_path_preserve_content | `archive/originals/6d4cdf924e8b6fe2.txt` |
| `distance-constrained-subtraction-games/src/distance_subtraction_research.cpp` | remove_old_path_preserve_content | `archive/originals/05fdd9c7c9e3422d.cpp` |
| `distance-constrained-subtraction-games/src/distance_subtraction_research.py` | remove_old_path_preserve_content | `archive/originals/9d39234e8247f570.py` |
| `distance-constrained-subtraction-games/src/full_state_analysis.py` | remove_old_path_preserve_content | `archive/originals/ec07c6b8fca37bd3.py` |
| `distance-subtraction-research-with-affine-extractor/.gitignore` | replace_at_same_path | `archive/originals/2d7eae050367577a` |
| `distance-subtraction-research-with-affine-extractor/AFFINE_ANALYSIS_GUIDE.md` | replace_at_same_path | `archive/originals/511b552e8c06d94c.md` |
| `distance-subtraction-research-with-affine-extractor/CHANGELOG.md` | replace_at_same_path | `archive/originals/4bb53f85b025a12c.md` |
| `distance-subtraction-research-with-affine-extractor/DISCOVERIES.md` | replace_at_same_path | `archive/originals/77afedd6503d2e6a.md` |
| `distance-subtraction-research-with-affine-extractor/GITHUB_PUSH_INSTRUCTIONS.md` | replace_at_same_path | `archive/originals/b1034de08498e718.md` |
| `distance-subtraction-research-with-affine-extractor/MANIFEST_SHA256.txt` | replace_at_same_path | `archive/originals/4715a24c78d9f79b.txt` |
| `distance-subtraction-research-with-affine-extractor/README.md` | replace_at_same_path | `archive/originals/9a7d3a6e4bd463d1.md` |
| `distance-subtraction-research-with-affine-extractor/REPRODUCIBILITY.md` | replace_at_same_path | `archive/originals/9a34fdd6f73c69c4.md` |
| `distance-subtraction-research-with-affine-extractor/requirements.txt` | replace_at_same_path | `archive/originals/6d4cdf924e8b6fe2.txt` |
| `distance-subtraction-research-with-row-interval-classifier/.gitignore` | replace_at_same_path | `archive/originals/2d7eae050367577a` |
| `distance-subtraction-research-with-row-interval-classifier/CHANGELOG.md` | replace_at_same_path | `archive/originals/83c132252250877a.md` |
| `distance-subtraction-research-with-row-interval-classifier/DISCOVERIES.md` | replace_at_same_path | `archive/originals/77afedd6503d2e6a.md` |
| `distance-subtraction-research-with-row-interval-classifier/GITHUB_PUSH_INSTRUCTIONS.md` | replace_at_same_path | `archive/originals/b1034de08498e718.md` |
| `distance-subtraction-research-with-row-interval-classifier/MANIFEST_SHA256.txt` | replace_at_same_path | `archive/originals/2394ea2738d0f15b.txt` |
| `distance-subtraction-research-with-row-interval-classifier/README.md` | replace_at_same_path | `archive/originals/b24886e7a6ee1043.md` |
| `distance-subtraction-research-with-row-interval-classifier/REPRODUCIBILITY.md` | replace_at_same_path | `archive/originals/9a34fdd6f73c69c4.md` |
| `distance-subtraction-research-with-row-interval-classifier/requirements.txt` | replace_at_same_path | `archive/originals/6d4cdf924e8b6fe2.txt` |
| `requirements.txt` | replace_at_same_path | `archive/originals/6d4cdf924e8b6fe2.txt` |

## research/formal-theorems-a-b-c

85 tracked paths audited.

| Old path | Proposed action | Original content retained at |
|---|---|---|
| `.gitignore` | replace_at_same_path | `archive/originals/2d7eae050367577a` |
| `AFFINE_ANALYSIS_GUIDE.md` | retain_same_path | `AFFINE_ANALYSIS_GUIDE.md` |
| `CHANGELOG.md` | replace_at_same_path | `archive/originals/a26d0e95e854f8a5.md` |
| `DISCOVERIES.md` | replace_at_same_path | `archive/originals/4d6e8962d82df54b.md` |
| `GITHUB_PUSH_INSTRUCTIONS.md` | replace_at_same_path | `archive/originals/b1034de08498e718.md` |
| `GITHUB_UPDATE_INSTRUCTIONS.md` | replace_at_same_path | `archive/originals/b0c86be564679dae.md` |
| `MANIFEST_SHA256.txt` | replace_at_same_path | `archive/originals/2d6019d32c13059f.txt` |
| `README.md` | replace_at_same_path | `archive/originals/a5f9aa342ef35f7e.md` |
| `REPRODUCIBILITY.md` | replace_at_same_path | `archive/originals/9a34fdd6f73c69c4.md` |
| `RESEARCH_UPDATE_CONCLUSION.md` | replace_at_same_path | `archive/originals/2c7c5761d0fdac4a.md` |
| `distance-constrained-subtraction-games/.gitignore` | remove_old_path_preserve_content | `archive/originals/2d7eae050367577a` |
| `distance-constrained-subtraction-games/CHANGELOG.md` | remove_old_path_preserve_content | `archive/originals/7bc4cedbd5cf0115.md` |
| `distance-constrained-subtraction-games/DISCOVERIES.md` | remove_old_path_preserve_content | `archive/originals/77afedd6503d2e6a.md` |
| `distance-constrained-subtraction-games/GITHUB_PUSH_INSTRUCTIONS.md` | remove_old_path_preserve_content | `archive/originals/b1034de08498e718.md` |
| `distance-constrained-subtraction-games/MANIFEST_SHA256.txt` | remove_old_path_preserve_content | `archive/originals/2fd56720d55b0335.txt` |
| `distance-constrained-subtraction-games/README.md` | remove_old_path_preserve_content | `archive/originals/28db47c0e5e3b692.md` |
| `distance-constrained-subtraction-games/REPRODUCIBILITY.md` | remove_old_path_preserve_content | `archive/originals/9a34fdd6f73c69c4.md` |
| `distance-constrained-subtraction-games/RESEARCH_UPDATE_CONCLUSION.md` | remove_old_path_preserve_content | `archive/originals/78ece2ce43852f19.md` |
| `distance-constrained-subtraction-games/THEOREM_C_VERIFICATION.md` | remove_old_path_preserve_content | `archive/originals/f501757bb46e28f6.md` |
| `distance-constrained-subtraction-games/THEOREM_STATUS.md` | remove_old_path_preserve_content | `archive/originals/f6828fde872b0d1b.md` |
| `distance-constrained-subtraction-games/archive/bash_test_results/literature_search_terms.txt` | remove_old_path_preserve_content | `archive/originals/a2522c66cc5411f6.txt` |
| `distance-constrained-subtraction-games/archive/bash_test_results/research_report.md` | remove_old_path_preserve_content | `archive/originals/b524298c15935238.md` |
| `distance-constrained-subtraction-games/archive/bash_test_results/scan_results.csv` | remove_old_path_preserve_content | `archive/originals/2496b9f781d7d3da.csv` |
| `distance-constrained-subtraction-games/archive/cpp_test_scan/literature_search_terms.txt` | remove_old_path_preserve_content | `archive/originals/a2522c66cc5411f6.txt` |
| `distance-constrained-subtraction-games/archive/cpp_test_scan/research_report.md` | remove_old_path_preserve_content | `archive/originals/d97db7385c2471b8.md` |
| `distance-constrained-subtraction-games/archive/cpp_test_scan/scan_results.csv` | remove_old_path_preserve_content | `archive/originals/5f05985fcad9fb26.csv` |
| `distance-constrained-subtraction-games/data/certificates/full_state_period_certificates_k58_78.csv` | remove_old_path_preserve_content | `archive/originals/e2a338f463b4e391.csv` |
| `distance-constrained-subtraction-games/data/certificates/theorem_C_boundary_counterexamples.csv` | remove_old_path_preserve_content | `archive/originals/197ae803e45b54f1.csv` |
| `distance-constrained-subtraction-games/data/certificates/theorem_C_certificates.csv` | remove_old_path_preserve_content | `archive/originals/0320cb5ccb85e6e7.csv` |
| `distance-constrained-subtraction-games/data/certificates/theorem_C_summary.json` | remove_old_path_preserve_content | `archive/originals/080026c0c89c3925.json` |
| `distance-constrained-subtraction-games/data/comparison/m0_m1_m2_k2_15_n10000_scan_results.csv` | remove_old_path_preserve_content | `archive/originals/2496b9f781d7d3da.csv` |
| `distance-constrained-subtraction-games/data/deep_scan/m1_35_80_scan_results.csv` | remove_old_path_preserve_content | `archive/originals/b99f57a2310ee099.csv` |
| `distance-constrained-subtraction-games/data/deep_scan/m1_81_120_scan_results.csv` | remove_old_path_preserve_content | `archive/originals/69500adf45029e43.csv` |
| `distance-constrained-subtraction-games/data/deep_scan/m1_deep_35_120.csv` | remove_old_path_preserve_content | `archive/originals/3df2c5f54d3139bd.csv` |
| `distance-constrained-subtraction-games/data/exploratory/m1_k5_100_n200000_scan_results.csv` | remove_old_path_preserve_content | `archive/originals/d301182c59539053.csv` |
| `distance-constrained-subtraction-games/docs/archive/AI Algorithm & Correctness Proof.docx` | remove_old_path_preserve_content | `docs/archive/AI Algorithm & Correctness Proof.docx` |
| `distance-constrained-subtraction-games/docs/distance_subtraction_methodology.md` | remove_old_path_preserve_content | `archive/originals/149e469cbe1e3b2d.md` |
| `distance-constrained-subtraction-games/figures/full_state_k68_p_positions.png` | remove_old_path_preserve_content | `figures/full_state_k68_p_positions.png` |
| `distance-constrained-subtraction-games/literature/literature_search_terms.txt` | remove_old_path_preserve_content | `archive/originals/a2522c66cc5411f6.txt` |
| `distance-constrained-subtraction-games/logs/compiler_error_missing_cpp17.md` | remove_old_path_preserve_content | `archive/originals/b4d44664ada81e25.md` |
| `distance-constrained-subtraction-games/paper/README.md` | remove_old_path_preserve_content | `archive/originals/fd8aa05b665d4e52.md` |
| `distance-constrained-subtraction-games/paper/SOURCE_AUDIT.md` | remove_old_path_preserve_content | `archive/originals/16b1671ada002a67.md` |
| `distance-constrained-subtraction-games/paper/WORKS_CITED.md` | remove_old_path_preserve_content | `archive/originals/2b8c6b92274c157a.md` |
| `distance-constrained-subtraction-games/paper/archive/main_before_theorem_split_2026-10-09.tex` | remove_old_path_preserve_content | `archive/originals/db7f6d1f985a2b93.tex` |
| `distance-constrained-subtraction-games/paper/main.pdf` | remove_old_path_preserve_content | `paper/main.pdf` |
| `distance-constrained-subtraction-games/paper/main.tex` | remove_old_path_preserve_content | `archive/originals/69286bb7c03e2a00.tex` |
| `distance-constrained-subtraction-games/paper/references.bib` | remove_old_path_preserve_content | `archive/originals/02485298e280ca5e.bib` |
| `distance-constrained-subtraction-games/paper/references.tex` | remove_old_path_preserve_content | `archive/originals/0ec321f1b512508b.tex` |
| `distance-constrained-subtraction-games/paper/shared/preamble.tex` | remove_old_path_preserve_content | `archive/originals/7b910286b46260ae.tex` |
| `distance-constrained-subtraction-games/paper/shared/works_cited.tex` | remove_old_path_preserve_content | `archive/originals/113baac109708777.tex` |
| `distance-constrained-subtraction-games/paper/theorem_A/body.tex` | remove_old_path_preserve_content | `archive/originals/cbfc03f67988d6b5.tex` |
| `distance-constrained-subtraction-games/paper/theorem_A/main.pdf` | remove_old_path_preserve_content | `paper/theorem_A/main.pdf` |
| `distance-constrained-subtraction-games/paper/theorem_A/main.tex` | remove_old_path_preserve_content | `archive/originals/9590d0a4045737f0.tex` |
| `distance-constrained-subtraction-games/paper/theorem_B/body.tex` | remove_old_path_preserve_content | `archive/originals/ab4eecefda386e2a.tex` |
| `distance-constrained-subtraction-games/paper/theorem_B/main.pdf` | remove_old_path_preserve_content | `paper/theorem_B/main.pdf` |
| `distance-constrained-subtraction-games/paper/theorem_B/main.tex` | remove_old_path_preserve_content | `archive/originals/635e6f155898c10f.tex` |
| `distance-constrained-subtraction-games/paper/theorem_C/body.tex` | remove_old_path_preserve_content | `archive/originals/dbc250a1930d55a5.tex` |
| `distance-constrained-subtraction-games/paper/theorem_C/main.pdf` | remove_old_path_preserve_content | `paper/theorem_C/main.pdf` |
| `distance-constrained-subtraction-games/paper/theorem_C/main.tex` | remove_old_path_preserve_content | `archive/originals/fe91f1f7bb2ce7fc.tex` |
| `distance-constrained-subtraction-games/reports/m1_deep_35_80_report.md` | remove_old_path_preserve_content | `archive/originals/455192afd052c73d.md` |
| `distance-constrained-subtraction-games/reports/m1_deep_81_120_report.md` | remove_old_path_preserve_content | `archive/originals/de34d781dde9619d.md` |
| `distance-constrained-subtraction-games/reports/m1_k5_100_n200000_report.md` | remove_old_path_preserve_content | `archive/originals/a8d653a7803bf198.md` |
| `distance-constrained-subtraction-games/requirements.txt` | remove_old_path_preserve_content | `archive/originals/6d4cdf924e8b6fe2.txt` |
| `distance-constrained-subtraction-games/src/distance_subtraction_research.cpp` | remove_old_path_preserve_content | `archive/originals/05fdd9c7c9e3422d.cpp` |
| `distance-constrained-subtraction-games/src/distance_subtraction_research.py` | remove_old_path_preserve_content | `archive/originals/9d39234e8247f570.py` |
| `distance-constrained-subtraction-games/src/full_state_analysis.py` | remove_old_path_preserve_content | `archive/originals/ec07c6b8fca37bd3.py` |
| `distance-constrained-subtraction-games/src/verify_theorem_c.py` | remove_old_path_preserve_content | `archive/originals/198b3a2c08bb8df0.py` |
| `distance-subtraction-research-with-affine-extractor/.gitignore` | replace_at_same_path | `archive/originals/2d7eae050367577a` |
| `distance-subtraction-research-with-affine-extractor/AFFINE_ANALYSIS_GUIDE.md` | replace_at_same_path | `archive/originals/511b552e8c06d94c.md` |
| `distance-subtraction-research-with-affine-extractor/CHANGELOG.md` | replace_at_same_path | `archive/originals/4bb53f85b025a12c.md` |
| `distance-subtraction-research-with-affine-extractor/DISCOVERIES.md` | replace_at_same_path | `archive/originals/77afedd6503d2e6a.md` |
| `distance-subtraction-research-with-affine-extractor/GITHUB_PUSH_INSTRUCTIONS.md` | replace_at_same_path | `archive/originals/b1034de08498e718.md` |
| `distance-subtraction-research-with-affine-extractor/MANIFEST_SHA256.txt` | replace_at_same_path | `archive/originals/4715a24c78d9f79b.txt` |
| `distance-subtraction-research-with-affine-extractor/README.md` | replace_at_same_path | `archive/originals/9a7d3a6e4bd463d1.md` |
| `distance-subtraction-research-with-affine-extractor/REPRODUCIBILITY.md` | replace_at_same_path | `archive/originals/9a34fdd6f73c69c4.md` |
| `distance-subtraction-research-with-affine-extractor/requirements.txt` | replace_at_same_path | `archive/originals/6d4cdf924e8b6fe2.txt` |
| `distance-subtraction-research-with-row-interval-classifier/.gitignore` | replace_at_same_path | `archive/originals/2d7eae050367577a` |
| `distance-subtraction-research-with-row-interval-classifier/CHANGELOG.md` | replace_at_same_path | `archive/originals/83c132252250877a.md` |
| `distance-subtraction-research-with-row-interval-classifier/DISCOVERIES.md` | replace_at_same_path | `archive/originals/77afedd6503d2e6a.md` |
| `distance-subtraction-research-with-row-interval-classifier/GITHUB_PUSH_INSTRUCTIONS.md` | replace_at_same_path | `archive/originals/b1034de08498e718.md` |
| `distance-subtraction-research-with-row-interval-classifier/MANIFEST_SHA256.txt` | replace_at_same_path | `archive/originals/2394ea2738d0f15b.txt` |
| `distance-subtraction-research-with-row-interval-classifier/README.md` | replace_at_same_path | `archive/originals/b24886e7a6ee1043.md` |
| `distance-subtraction-research-with-row-interval-classifier/REPRODUCIBILITY.md` | replace_at_same_path | `archive/originals/9a34fdd6f73c69c4.md` |
| `distance-subtraction-research-with-row-interval-classifier/requirements.txt` | replace_at_same_path | `archive/originals/6d4cdf924e8b6fe2.txt` |
| `requirements.txt` | replace_at_same_path | `archive/originals/6d4cdf924e8b6fe2.txt` |

