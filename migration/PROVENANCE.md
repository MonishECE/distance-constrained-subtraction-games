# Source and completeness audit

Remote source: https://github.com/MonishECE/distance-constrained-subtraction-games
Pinned commits and branches: BRANCH_SNAPSHOT.json. Every file on both heads is mapped in DELETION_AUDIT.csv and retained unchanged either canonically or in archive/branch-originals. Original Git history is in archive/repository-history.bundle (both branch heads). No GitHub mutation was performed.

Additional recovered source: ZIP blob at c8b69f4:distance-subtraction-research-with-affine-extractor.zip (later deleted at 6c30d32). Its missing affine script, results and logs are restored. Initial paper recovered byte-for-byte from 7fd277c, authored 2026-10-03 UTC; older documentation's October 4 date is not used as a Git fact.

Unavailable: original verify_theorems_ab.py, theorem_B_audit data, PROOF_AUDIT.md, row_interval_classifier.py, and row-interval output tables. They are referenced in documentation but absent from every accessible commit and recovered ZIP. Cached prior chat and read_thread return assistant reference markers only; no accessible attachments. This ZIP cannot claim to recover those missing originals. A newly authored A/B verifier and its generated certificates repair the C import dependency using the documented recurrence; a new proof audit records that change.

Upstream compiled PDFs are preserved, not relabeled as newly generated PDFs. Canonical LaTeX math and bibliography are retained. Old provenance statements in archived documents are historical and may be stale. Affine extraction remains finite evidence with residual points, not a uniform proof.

Citation retrieval on 2026-10-10: Sprague journal record was opened and confirms 1935, vol.41, pp.438–444; Grundy's linked two-page scan was accessible; Gurvich's author publication list was accessible. Routledge record failed retrieval, so its upstream citation metadata is retained but not newly confirmed. No broad novelty/priority audit was performed. See paper/CITATION_RECHECK.md.
