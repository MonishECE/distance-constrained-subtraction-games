# Validation report — October 10, 2026

Remote branch heads reconfirmed after assembly: main 35419ed7c83871110afea2399a0493c2c06a2674; research/formal-theorems-a-b-c 74afe5d0fb015b8d12fcbbe45e628976c388cf54. No remote mutation.

Completed checks:

- Optimized Python SG engine self-test against its slow solver: PASS.
- Recovered affine extractor self-test: Boolean/SG, exact affine fits and k=68 exact cover/certificate: PASS.
- Rebuilt A/B verifier: 60 (k,m) parameter combinations with direct Boolean and SG comparisons through n=100; 21 B window/bridge certificates, SG and naive comparison, exhaustive least-period check: PASS.
- C verifier: 12 fixed-parameter certificates, independent SG checks and 8 naive-checked boundary counterexamples: PASS.
- Existing full-state certificate generator: 21 cases with independent SG comparison: PASS.
- All generated CSV/JSON certificate files reproduce byte-for-byte; B/C witness and boundary tables match LaTeX. Additional exhaustive C residue-pattern minimality check: PASS.
- Every one of the 145 branch-file audit rows points to retained original content with the exact source SHA-256. Manifest accounts for every package file except itself: PASS.
- All four single-file Overleaf sources contain no external file inputs. Integrated, theorem A, B and C files compiled successfully with the desktop LaTeX compiler. Modular paper sources were expanded directly into those tested standalone files; local multi-file pdflatex was unavailable.
- Complete historical Git bundle verified by Git: PASS.
- Migration dry run and actual replacement exercised in a disposable copy of the cloned repository on a new branch. Backup bundle created; post-replacement package verification and staged-file coverage checked. Original-branch guard and dirty-checkout guard tested: PASS.
- ZIP CRC, single top-level folder, path safety, exact extracted bytes and verification in the extracted folder: PASS (final packaging check).

Limits: no C++ compiler was available, so C++17 compilation/self-test was not run. N=500,000 exploratory scans and the complete affine batch were not rerun. The built-in compiler confirms successful compilation but does not export PDF files; supplied upstream PDFs are retained and are not represented as newly rendered outputs. A visual page-by-page PDF review was not performed. Missing original row-interval artifacts and A/B code are disclosed in PROVENANCE.md. Tests check finite premises and consistency, not a formal proof assistant verification or a novelty claim.
