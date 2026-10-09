# Research conclusion and audit trail — October 9, 2026

Theorem folders and sources are now individually maintained under `paper/theorem_A`, `paper/theorem_B`, `paper/theorem_C`. The integrated `paper/main.tex` is a reproducible undergraduate-style manuscript. All old research and historical paper sources are preserved in this update.

Process: inspected the earlier A/B paper and its audits; formalized theorem-A interval and finite-memory arguments; reused the verified 21 finite-k B certificates and corrected bridge bounds; independently verified the previously observational A=54 affine family for all k=42..53; discovered and proved the period-degeneracy criterion at k=A-1; proved a universal necessary bound k<A for the proposed three-residue template; constructed eight first-mismatch counterexamples; audited external citations against journal, publisher, author's bibliography, and bibliography scan indexes; and generated four standalone/integrated LaTeX manuscripts.

**Proof conclusion.** Theorem A is proved for all fixed game parameters. Theorem B is proved for 21 fixed integer k by finite verified premises and induction, not a uniform symbolic derivation. Theorem C now includes new universal arithmetic lemmas and 12 fixed-k computer-assisted cases, but the general parameter-hierarchy theorem is **Working on**. The numbers 54 and 86, and termination at k=78, are not derived uniformly from the recurrence. We cannot infer an infinite hierarchy from two families.

**Literature provenance.** Cited sources provide mathematical context and an adjacent game variant; no third-party proof is presented as an original theorem. The paper has a Works cited section, and `paper/SOURCE_AUDIT.md` records where each bibliographic detail was independently checked. Completeness of novelty review remains **Working on**.

Verification: `python src/verify_theorems_ab.py`, `python src/verify_theorem_c.py`, extractor self-tests, LaTeX compilation, and source path audit. Confirm results in final work log before committing.
