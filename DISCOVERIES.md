# Current Discoveries and Research Status

This file is the current mathematical status record. It deliberately
separates finite computation, exact computer-assisted certification, and
unproved symbolic claims.

## 1. Main game

The main object is (D(k,1)). After a move of size (s), the next removal
(r) must satisfy

\[ \|r-s\|\>1. \]

A full state is ((n,s)).

## 2. Deep-scan observations

The main C++ scan covered

\[ 35`\le `{=tex}k`\le120`{=tex},`\qquad `{=tex}N=500{,}000. \]

### Observed affine regime A

For every tested

\[ 42`\le `{=tex}k`\le52`{=tex}, \]

the starting sequence had candidate period

\[ p=2k+56 \]

with P-residues

\[ {0,54,k+55}`\pmod{2k+56}`{=tex}. \]

This is strongly validated computationally but has not yet received the
same standalone finite-state certificate treatment as the second regime.

### Observed and certified affine regime B

For

\[ 58`\le `{=tex}k`\le78`{=tex}, \]

the starting P-position formula is

\[ `\boxed{
p=2k+88,\qquad
P_{\mathrm{start}}\equiv\{0,86,k+87\}\pmod{2k+88}.
}`{=tex} \]

The formula first appeared as a deep-scan pattern and was subsequently
subjected to an independent Boolean full-state analysis.

## 3. Exact finite-state certification for (58`\le `{=tex}k`\le78`{=tex})

For fixed (k), write the complete Boolean P/N row as

\[ R_n=(P(n,1),`\ldots`{=tex},P(n,k)). \]

The recurrence for (R_n) depends only on the preceding (k) rows.
Therefore, if

\[ R\_{t+i}=R\_{t+p+i} `\qquad`{=tex}(0`\le `{=tex}i\<k), \]

then determinism forces

\[ R_n=R\_{n+p}`\qquad`{=tex}(n`\ge `{=tex}t). \]

The standalone Python verifier finds such a repeated (k)-row state
window for all 21 values (58`\le `{=tex}k`\le78`{=tex}) with

\[ p=2k+88. \]

For (65`\le `{=tex}k`\le78`{=tex}), the full Boolean state cycle begins
at (t=0). For (58`\le `{=tex}k`\le64`{=tex}), a short full-state
transient occurs, with the cycle beginning at (t=58) or (59).

The unrestricted starting sequence is separately checked over a finite
prefix through

\[ t+k+p-1, \]

which covers one complete starting-position period after the full-state
cycle is active. This establishes the claimed starting residue formula
for each of the 21 fixed (k)-values.

The Boolean states are also cross-checked against an independent direct
Sprague-Grundy solver over the finite certificate range.

**Status:** exact computer-assisted finite-range certification.

**Not yet established:** one symbolic proof explaining all
(58`\le `{=tex}k`\le78`{=tex}) simultaneously, or a general theorem
explaining why the boundaries are 58 and 78.

## 4. Boolean reformulation

Define

\[ A_n={r:(n-r,r)`\text{ is a P-state}`{=tex}}. \]

Then the unrestricted start at heap size (n) is P iff

\[ A_n=`\varnothing`{=tex}. \]

For (m=1),

\[ (n,s)`\text{ is P}`{=tex} `\iff`{=tex}
A_n`\subseteq`{=tex}{s-1,s,s+1}, \]

after clipping the forbidden move set to (1,`\ldots`{=tex},k).

This removes the need to reason about nonzero Grundy values when the
objective is only P/N classification.

## 5. Full-state geometry

The representative (k=68) state plot has

\[ p=224,`\qquad`{=tex}
P\_{`\mathrm{start}`{=tex}}`\equiv`{=tex}{0,86,155}`\pmod{224}`{=tex}.
\]

The full P-state diagram contains repeated diagonal and vertical
structures rather than unstructured noise. Preliminary inspection shows
fixed and parameter-dependent components.

This motivates exact affine-region extraction.

## 6. Important stress-test result: (k=80)

A shorter computation previously suggested a large preperiod near
(99{,}685).

The (N=500{,}000) computation instead produced candidate

\[ `\text{preperiod}`{=tex}=0,`\qquad `{=tex}p=947, \]

with starting residues

\[ {0,86,168,249,785,866}`\pmod{947}`{=tex}. \]

The earlier interpretation is therefore retained only as a
methodological example of why finite-tail period detection must be
stress-tested.

## 7. Other observed behavior

A simple block occurs around

\[ 93`\le `{=tex}k`\le99`{=tex} \]

with candidate (p=k+1) and starting residue ({0}). At (k=100), the
period remains (101) in the deep scan but a nonzero preperiod appears.

Another simple block begins at least over

\[ 117`\le `{=tex}k`\le120`{=tex} \]

with (p=k+1) and residue ({0}); the scan ended at (120), so its upper
boundary is not yet known.

Large/irregular examples include

\[ p(80)=947,`\qquad `{=tex}p(81)=597,`\qquad `{=tex}p(107)=1370. \]

These are interesting complexity markers but are not the current proof
targets.

## 8. Working structural hypothesis

The current hypothesis is that (k) passes through distinct structural
regimes in which period lengths and P-position residues admit simple
affine descriptions.

The two observed three-residue regimes share the template

\[ p=2k+A+2, `\qquad`{=tex}
P\_{`\mathrm{start}`{=tex}}`\equiv`{=tex}{0,A,k+A+1}`\pmod `{=tex}p, \]

with observed (A=54) and (A=86).

The difference (86-54=32) is suggestive only. No recurrence for (A),
binary/2-adic explanation, or infinite family has been proved.

## 9. Immediate next step

Perform exact affine-region extraction on full P-state coordinates.

For each connected or structurally coherent component, test exact
invariants such as

\[ n-s=C,`\qquad `{=tex}n-2s=C,`\qquad `{=tex}n+s=C, \]

and determine exact endpoint formulas.

Then track each component across (58`\le `{=tex}k`\le78`{=tex}),
classifying its intercepts and endpoints as constant, affine in (k), or
unresolved.

The desired output is a symbolic candidate

\[
`\mathcal `{=tex}P_k=R_1(k)`\cup`{=tex}`\cdots`{=tex}`\cup `{=tex}R_q(k)
\]

that matches every certified state.

The mathematical proof stage then attempts to show:

\[ P`\not`{=tex}`\to `{=tex}P \]

and

\[ N`\to `{=tex}P. \]

## 10. Claims discipline

Use these labels consistently:

-   **Observed:** supported by finite computation.
-   **Certified for fixed (k):** forced indefinitely by a verified
    finite-state recurrence/cycle certificate.
-   **Conjectured:** symbolic pattern inferred from the data but not
    proved.
-   **Proved:** established by a mathematical argument independent of
    extending the computation.

Do not describe literature novelty as established until the dedicated
literature review is complete.
