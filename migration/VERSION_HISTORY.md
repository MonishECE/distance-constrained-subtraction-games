# Version and folder history

- main: `35419ed7c83871110afea2399a0493c2c06a2674`
- research/formal-theorems-a-b-c: `74afe5d0fb015b8d12fcbbe45e628976c388cf54`

The repository records commits, not release tags. Original nested base package: original SG engines, full-state certificates, data and draft paper. Affine folder: documentation only in current branches; its actual script/results/logs recovered from the historical ZIP. Row-interval folder: documentation only; classifier/results unavailable. Research branch: adds split A/B/C LaTeX, citations, supplied PDFs and C script/evidence, but omits its A/B import dependency. Clean package resolves the nesting and dependency while preserving originals.

```text
7fd277c67f6e84e8531e689e5b3a81562106a32b 2026-10-03T20:48:15-05:00 Initial computational research repository

 distance-constrained-subtraction-games/.gitignore  |  26 +
 .../CHANGELOG.md                                   |  25 +
 .../DISCOVERIES.md                                 | 231 +++++
 .../GITHUB_PUSH_INSTRUCTIONS.md                    | 155 ++++
 .../MANIFEST_SHA256.txt                            |  34 +
 distance-constrained-subtraction-games/README.md   | 184 ++++
 .../REPRODUCIBILITY.md                             | 124 +++
 .../bash_test_results/literature_search_terms.txt  |   6 +
 .../archive/bash_test_results/research_report.md   |  45 +
 .../archive/bash_test_results/scan_results.csv     |  43 +
 .../cpp_test_scan/literature_search_terms.txt      |   6 +
 .../archive/cpp_test_scan/research_report.md       |  38 +
 .../archive/cpp_test_scan/scan_results.csv         |  10 +
 .../full_state_period_certificates_k58_78.csv      |  22 +
 .../m0_m1_m2_k2_15_n10000_scan_results.csv         |  43 +
 .../data/deep_scan/m1_35_80_scan_results.csv       |  47 +
 .../data/deep_scan/m1_81_120_scan_results.csv      |  41 +
 .../data/deep_scan/m1_deep_35_120.csv              |  87 ++
 .../exploratory/m1_k5_100_n200000_scan_results.csv |  97 ++
 .../archive/AI Algorithm & Correctness Proof.docx  | Bin 0 -> 157397 bytes
 .../docs/distance_subtraction_methodology.md       | 965 ++++++++++++++++++++
 .../figures/full_state_k68_p_positions.png         | Bin 0 -> 61774 bytes
 .../literature/literature_search_terms.txt         |   6 +
 .../logs/compiler_error_missing_cpp17.md           | 477 ++++++++++
 .../paper/main.tex                                 | 984 +++++++++++++++++++++
 .../reports/m1_deep_35_80_report.md                |  45 +
 .../reports/m1_deep_81_120_report.md               |  44 +
 .../reports/m1_k5_100_n200000_report.md            |  40 +
 .../requirements.txt                               |   2 +
 .../src/distance_subtraction_research.cpp          | 903 +++++++++++++++++++
 .../src/distance_subtraction_research.py           | 831 +++++++++++++++++
 .../src/full_state_analysis.py                     | 205 +++++
 32 files changed, 5766 insertions(+)
c8b69f467021b64269e0c64ae72024587fe8818a 2026-10-09T10:22:38-05:00 Add files via upload

 ...ance-subtraction-research-with-affine-extractor.zip | Bin 0 -> 207233 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)
6c30d32d5e36d2121baa4952a97a85dae2386f95 2026-10-09T10:23:06-05:00 Delete distance-subtraction-research-with-affine-extractor.zip

 ...ance-subtraction-research-with-affine-extractor.zip | Bin 207233 -> 0 bytes
 1 file changed, 0 insertions(+), 0 deletions(-)
8b68f76bea671dc3be3c48c0283b22c251ebaab8 2026-10-09T10:23:43-05:00 Add files via upload

 .gitignore                  |  26 +++++
 AFFINE_ANALYSIS_GUIDE.md    |  51 ++++++++++
 CHANGELOG.md                |  33 +++++++
 DISCOVERIES.md              | 231 ++++++++++++++++++++++++++++++++++++++++++++
 GITHUB_PUSH_INSTRUCTIONS.md | 155 +++++++++++++++++++++++++++++
 MANIFEST_SHA256.txt         |  54 +++++++++++
 README.md                   | 197 +++++++++++++++++++++++++++++++++++++
 REPRODUCIBILITY.md          | 124 ++++++++++++++++++++++++
 requirements.txt            |   2 +
 9 files changed, 873 insertions(+)
fd673bd3048ceb42c5f7cd58b5d08730c861eb37 2026-10-09T10:25:41-05:00 uploads

 .../.gitignore                                                            | 0
 .../AFFINE_ANALYSIS_GUIDE.md                                              | 0
 .../CHANGELOG.md                                                          | 0
 .../DISCOVERIES.md                                                        | 0
 .../GITHUB_PUSH_INSTRUCTIONS.md                                           | 0
 .../MANIFEST_SHA256.txt                                                   | 0
 .../README.md                                                             | 0
 .../REPRODUCIBILITY.md                                                    | 0
 .../requirements.txt                                                      | 0
 9 files changed, 0 insertions(+), 0 deletions(-)
28212744719393930adae90371b7151f982b8437 2026-10-09T10:59:49-05:00 row interval classifier

 .gitignore                  |  26 +++++
 CHANGELOG.md                |  25 +++++
 DISCOVERIES.md              | 231 ++++++++++++++++++++++++++++++++++++++++++++
 GITHUB_PUSH_INSTRUCTIONS.md | 155 +++++++++++++++++++++++++++++
 MANIFEST_SHA256.txt         |  34 +++++++
 README.md                   | 184 +++++++++++++++++++++++++++++++++++
 REPRODUCIBILITY.md          | 124 ++++++++++++++++++++++++
 requirements.txt            |   2 +
 8 files changed, 781 insertions(+)
a28b3df0392c9e3ffa64668ab67a03cbcf7bd4c7 2026-10-09T11:02:39-05:00 row interval classifer

 .../.gitignore                                                            | 0
 .../CHANGELOG.md                                                          | 0
 .../DISCOVERIES.md                                                        | 0
 .../GITHUB_PUSH_INSTRUCTIONS.md                                           | 0
 .../MANIFEST_SHA256.txt                                                   | 0
 .../README.md                                                             | 0
 .../REPRODUCIBILITY.md                                                    | 0
 .../requirements.txt                                                      | 0
 8 files changed, 0 insertions(+), 0 deletions(-)
35419ed7c83871110afea2399a0493c2c06a2674 2026-10-09T11:27:21-05:00 Completed updated research

 .gitignore                    |  26 +++++
 AFFINE_ANALYSIS_GUIDE.md      |  51 +++++++++
 CHANGELOG.md                  |  51 +++++++++
 DISCOVERIES.md                | 242 ++++++++++++++++++++++++++++++++++++++++++
 GITHUB_PUSH_INSTRUCTIONS.md   | 155 +++++++++++++++++++++++++++
 GITHUB_UPDATE_INSTRUCTIONS.md |  63 +++++++++++
 MANIFEST_SHA256.txt           |  74 +++++++++++++
 README.md                     | 223 ++++++++++++++++++++++++++++++++++++++
 REPRODUCIBILITY.md            | 124 ++++++++++++++++++++++
 RESEARCH_UPDATE_CONCLUSION.md |  37 +++++++
 requirements.txt              |   2 +
 11 files changed, 1048 insertions(+)
74afe5d0fb015b8d12fcbbe45e628976c388cf54 2026-10-09T12:21:08-05:00 Formalize Theorems A B C and update undergraduate research paper

 .../CHANGELOG.md                                   |  33 +
 .../MANIFEST_SHA256.txt                            | 123 ++-
 distance-constrained-subtraction-games/README.md   |  46 +
 .../RESEARCH_UPDATE_CONCLUSION.md                  |  11 +
 .../THEOREM_C_VERIFICATION.md                      |  46 +
 .../THEOREM_STATUS.md                              |  15 +
 .../theorem_C_boundary_counterexamples.csv         |   9 +
 .../data/certificates/theorem_C_certificates.csv   |  13 +
 .../data/certificates/theorem_C_summary.json       |  13 +
 .../paper/README.md                                |  31 +
 .../paper/SOURCE_AUDIT.md                          |   8 +
 .../paper/WORKS_CITED.md                           |  10 +
 .../main_before_theorem_split_2026-10-09.tex       | 474 ++++++++++
 .../paper/main.pdf                                 | Bin 0 -> 273229 bytes
 .../paper/main.tex                                 | 995 +--------------------
 .../paper/references.bib                           |  34 +
 .../paper/references.tex                           |   3 +
 .../paper/shared/preamble.tex                      |  21 +
 .../paper/shared/works_cited.tex                   |  17 +
 .../paper/theorem_A/body.tex                       |  36 +
 .../paper/theorem_A/main.pdf                       | Bin 0 -> 262562 bytes
 .../paper/theorem_A/main.tex                       |  12 +
 .../paper/theorem_B/body.tex                       |  53 ++
 .../paper/theorem_B/main.pdf                       | Bin 0 -> 276616 bytes
 .../paper/theorem_B/main.tex                       |  13 +
 .../paper/theorem_C/body.tex                       |  81 ++
 .../paper/theorem_C/main.pdf                       | Bin 0 -> 291035 bytes
 .../paper/theorem_C/main.tex                       |  14 +
 .../src/verify_theorem_c.py                        |  86 ++
 29 files changed, 1185 insertions(+), 1012 deletions(-)

```
