# Consolidation proof and computation audit

This is a new audit, not a recovery of the unavailable original PROOF_AUDIT.md.

Theorem A derives Q_n by intersecting all forbidden intervals for removals reaching P-children. The rebuilt interval solver implements this formula with exact bitsets. A direct legal-move Boolean solver and the existing direct mex/SG solver cross-check 60 small (k,m) pairs, including m=0, m>=k, k=1, and terminal heap n=0.

Theorem B requires k identical row pairs at displacement p and a starting formula checked through **t+k+p-1 inclusive**. The rebuilt verifier checks all 21 parameters, independent SG and naive outcomes, continuation of row repetition in an additional finite range, and exhaustive cyclic-shift minimality. Paper table witnesses are compared to newly generated CSV rows.

Theorem C retains its upstream verifier, importing the rebuilt recurrence and naive solver. It checks 12 fixed k values and 8 boundary counterexamples; upstream tables are compared to regenerated evidence. k=53 has displayed modulus 162 and least starting period 54. Minimality comes from the paper's analytic translation argument; additional tests can exhaust cyclic shifts of the claimed residue pattern.

Finite checks verify premises. The induction and analytic arguments in the paper supply the infinite-n consequences; these tests do not mechanically prove mathematical prose or establish originality. Uniform parameter explanations remain open. Affine catalogs with residual points are finite descriptions, not symbolic regime proofs.
