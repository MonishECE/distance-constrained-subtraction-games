# Distance-Constrained Dynamic Subtraction Games

## Research Question, Methodology, and Computational Findings to Date

**Project area:** Combinatorial Game Theory / Discrete Mathematics\
**Current main case:** (D(k,1))\
**Status:** Computational discovery and validation phase completed for
the main observed regimes; proof-oriented full-state analysis is
beginning.

------------------------------------------------------------------------

## 1. Research Question

### Primary research question

**How does imposing a minimum separation between consecutive move sizes
change the periodic structure of losing positions in a dynamic
subtraction game?**

More specifically, for the game (D(k,m)), we investigate:

> For fixed move bound (k) and move-separation parameter (m), what are
> the P-positions (previous-player winning / next-player losing
> positions), do they become eventually periodic, and can their periods
> and residue classes be classified as functions of (k) and (m)?

### Current focused question

The main investigation is now concentrated on (m=1):

> **For (D(k,1)), can the observed affine families of periods and
> P-position residues be explained and proved from the full state
> structure ((n,s))?**

A stronger long-term question is whether there is a parameterized family
of regimes of the form

\[ p(k)=2k+A+2, `\qquad`{=tex} P_k
`\equiv`{=tex}{0,A,k+A+1}`\pmod{p(k)}`{=tex}, \]

with mathematically describable values of (A) and corresponding ranges
of (k).

------------------------------------------------------------------------

## 2. Definition of the Game

We define a family of impartial combinatorial games (D(k,m)).

-   A single heap initially contains (n) counters.
-   On each turn, a player removes an integer number \[
    r`\in`{=tex}{1,2,`\ldots`{=tex},k}, \] subject to (r`\le`{=tex}n).
-   If the previous move removed (s) counters, the next move must
    satisfy \[ \|r-s\|\>m. \]
-   The first move is unrestricted by a previous move.
-   Normal play is used: a player with no legal move loses, even if
    counters remain in the heap.

The parameter (k) controls the largest possible removal. The parameter
(m) controls how different the next move must be from the previous move.

Important cases studied so far:

-   (m=0): consecutive moves cannot be equal; used as a known/control
    baseline.
-   (m=1): consecutive move sizes must differ by at least 2; this is the
    main research case.
-   (m=2): exploratory comparison/generalization.

------------------------------------------------------------------------

## 3. State-Space Model

Because legal moves depend on the previous move, the heap size (n) alone
is not enough to determine the game state.

After the first move, a state is represented as

\[ (n,s), \]

where:

-   \(n\) is the number of counters remaining;
-   \(s\) is the number of counters removed on the previous move.

From ((n,s)), a move of size (r) is legal when

\[ 1`\le`{=tex}r`\le`{=tex}`\min`{=tex}(k,n) \]

and

\[ \|r-s\|\>m. \]

The resulting state is

\[ (n-r,r). \]

This enlarged state representation converts the history-dependent rule
into a memoryless directed game graph.

------------------------------------------------------------------------

## 4. Sprague-Grundy Recurrence

For every state ((n,s)), define the Sprague-Grundy value (g(n,s)).

The legal child states are

\[ (n-r,r) \]

for every legal (r). Therefore,

\[ g(n,s)= `\operatorname{mex}`{=tex} `\left`{=tex}{ g(n-r,r):
1`\le`{=tex}r`\le`{=tex}`\min`{=tex}(k,n), \|r-s\|\>m `\right`{=tex}}.
\]

Here, (`\operatorname{mex}`{=tex}) is the minimum excluded nonnegative
integer.

A state is a P-position exactly when

\[ g(n,s)=0. \]

For the unrestricted starting position, define

\[ g_0(n)= `\operatorname{mex}`{=tex} `\left`{=tex}{ g(n-r,r):
1`\le`{=tex}r`\le`{=tex}`\min`{=tex}(k,n) `\right`{=tex}}. \]

Thus an initial heap size (n) is a starting P-position exactly when

\[ g_0(n)=0. \]

The binary starting P/N sequence is recorded as

\[ b_n=

```{=tex}
\begin{cases}
1,&g_0(n)=0,\\
0,&g_0(n)\ne0.
\end{cases}
```
\]

------------------------------------------------------------------------

## 5. Reference Solver

A direct reference solver was implemented first.

For each (n), each previous move (s), and each possible removal (r), the
solver explicitly tests whether

\[ \|r-s\|\>m. \]

It collects the SG values of every legal child and computes the mex
directly.

This solver is intentionally simple. Its main purpose is not speed but
independent correctness checking.

------------------------------------------------------------------------

## 6. Optimized Solver

The optimized solver uses the fact that, for fixed (n), the potential
child value associated with removing (r) is

\[ v_r=g(n-r,r). \]

For an unrestricted starting state, all valid (r) are available.

For a state with previous move (s), only the interval

\[ s-m`\le`{=tex}r`\le`{=tex}s+m \]

is forbidden, after clipping to the legal move range.

The optimized method therefore:

1.  Computes the SG values (v_r) for all possible removals.
2.  Counts the occurrences of each child SG value.
3.  Computes the unrestricted mex.
4.  For each previous move (s), temporarily removes the at-most-(2m+1)
    forbidden move contributions.
5.  Updates the mex after those removals.
6.  Stores (g(n,s)).
7.  Restores the removed contributions before processing the next (s).

For fixed small (m), the approximate time complexity is

\[ O(Nk(m+1)). \]

For the main case (m=1), this is approximately

\[ O(Nk) \]

up to constant factors.

The full stored SG table uses approximately

\[ O(Nk) \]

memory.

------------------------------------------------------------------------

## 7. Independent Verification

The optimized implementation was not accepted solely because it produced
plausible sequences.

A separate slow reference implementation was used for automated
self-tests on small parameter values.

The two implementations were compared across small values of (k), (m),
and (n), checking both:

-   the full state values (g(n,s));
-   the unrestricted starting values (g_0(n)).

The C++ research implementation passed these self-tests before deep
scans were performed.

This verification step was included to reduce the possibility that an
optimization error could create false mathematical patterns.

------------------------------------------------------------------------

## 8. Python and C++ Research Workflow

The project began with a Python research implementation because Python
allowed rapid development and inspection of the recurrence, P-position
sequences, periods, and residues.

After the computational range became large, the same research engine was
ported to C++17 for faster deep scans.

The C++ implementation retained:

-   SG computation;
-   starting P/N sequence generation;
-   candidate eventual-period detection;
-   residue extraction;
-   affine period-law mining;
-   contiguous affine-regime detection;
-   unusual-case detection;
-   optional full-state cycle detection;
-   CSV output;
-   automated research reports;
-   independent self-tests.

Python remains useful for the present proof-discovery stage because it
allows flexible analysis of the full ((n,s)) state structure and
symbolic pattern exploration.

------------------------------------------------------------------------

## 9. Period Detection Method

For each fixed pair ((k,m)), the starting P/N sequence

\[ b_0,b_1,`\ldots`{=tex},b_N \]

was generated.

A period detector searched for candidate periods (p) such that a
sufficiently long computed tail satisfies

\[ b_n=b\_{n+p}. \]

The detector requires repeated copies of the candidate period and then
searches backward to estimate the candidate preperiod.

When a candidate period is detected, the program records:

-   candidate preperiod;
-   candidate period (p);
-   P-position density within the period;
-   P-position residues modulo (p);
-   maximum observed SG values;
-   a fingerprint of the repeating word.

### Important limitation

A finite repeating tail is **not a mathematical proof** of eventual
periodicity.

All period statements produced by this detector are treated as
computational observations or conjectures until proved from the
recurrence or certified by an appropriate exact-state argument.

------------------------------------------------------------------------

## 10. Control and Comparative Experiments

The study compared (m=0), (m=1), and (m=2).

### (m=0)

For (m=0), the rule becomes

\[ r`\ne`{=tex}s. \]

This repetition-free case provides a control/baseline. The program
rediscovered highly structured period behavior in this case, supporting
the validity of the computational approach while also demonstrating that
known/control behavior should not be treated as a new result.

### (m=1)

The (m=1) case produced a mixture of simple periodic blocks, long
periods, abrupt transitions, and especially clean affine regimes. It was
therefore selected as the main research focus.

### (m=2)

The (m=2) case was explored as a generalization and comparison. It also
showed complex behavior, but the current proof effort is intentionally
concentrated on (m=1) to keep the mathematical scope manageable.

------------------------------------------------------------------------

## 11. Pattern-Mining Procedure

Two main automated pattern searches were used.

### 11.1 Affine laws across parameter classes

The program searched for relationships of the form

\[ p(k)=ak+b \]

among sets of parameter values.

### 11.2 Contiguous affine regimes

A second detector was added to identify consecutive intervals of (k) for
which the same affine period formula holds.

This was necessary because a search based only on global congruence
classes can miss a formula that is valid only on one consecutive range.

The contiguous search led to the main observed (m=1) regimes.

------------------------------------------------------------------------

## 12. Main Computational Findings So Far

All statements in this section are **observed computational patterns
unless explicitly stated otherwise**.

### 12.1 First affine regime

For

\[ 42`\le`{=tex}k`\le52`{=tex}, \]

the deep computations support

\[ `\boxed{p(k)=2k+56}`{=tex} \]

with starting P-position residues

\[ `\boxed{ P_k\equiv\{0,54,k+55\}\pmod{2k+56}. }`{=tex} \]

The P-position density within the candidate period is therefore

\[ `\frac{3}{2k+56}`{=tex}. \]

### 12.2 Second affine regime

For

\[ 58`\le`{=tex}k`\le78`{=tex}, \]

the deep computations support

\[ `\boxed{p(k)=2k+88}`{=tex} \]

with starting P-position residues

\[ `\boxed{ P_k\equiv\{0,86,k+87\}\pmod{2k+88}. }`{=tex} \]

The P-position density is

\[ `\frac{3}{2k+88}`{=tex}. \]

This regime contains 21 consecutive values of (k), making it the current
primary theorem candidate.

### 12.3 Common template

The two regimes share the form

\[ `\boxed{ p=2k+A+2 }`{=tex} \]

and

\[ `\boxed{ P_k\equiv\{0,A,k+A+1\}\pmod p. }`{=tex} \]

The observed constants are

\[ A=54 \]

and

\[ A=86. \]

Their difference is

\[ 86-54=32. \]

This numerical relationship is currently only suggestive. No recurrence
or binary/2-adic explanation has been proved.

------------------------------------------------------------------------

## 13. Observed Boundary Behavior

The clean affine laws do not continue universally.

Immediately after the second regime:

\[ k=79 \]

has an observed candidate period of

\[ 166 \]

with a nonzero preperiod, while

\[ k=80 \]

has a much larger observed candidate period

\[ 947. \]

This abrupt change suggests that the affine formulas belong to genuine
parameter regimes whose boundaries must be explained.

Other observed simple blocks include a region around

\[ 93`\le`{=tex}k`\le99`{=tex} \]

with

\[ p=k+1 \]

and starting residue ({0}).

At (k=100), the observed period remains (101), but a nonzero preperiod
appears, showing that period length alone does not capture the full
structure.

A further simple block was observed beginning at approximately

\[ 117`\le`{=tex}k`\le120`{=tex}, \]

again with

\[ p=k+1 \]

and residue ({0}). The scan ended at (k=120), so the upper boundary of
this block has not yet been determined.

------------------------------------------------------------------------

## 14. Deep Validation Experiment

The principal deep validation scan used

\[ m=1, `\qquad 35`{=tex}`\le`{=tex}k`\le120`{=tex}, `\qquad`{=tex}
N=500{,}000, \]

with candidate periods searched up to

\[ 150{,}000. \]

The execution was divided into two independent ranges because of a
runtime limit:

\[ 35`\le`{=tex}k`\le80`{=tex} \]

and

\[ 81`\le`{=tex}k`\le120`{=tex}. \]

Each (k) is computed independently, so splitting the range does not
change the recurrence or the resulting data.

The two principal affine regimes continued to appear through this much
larger computational horizon.

This provides substantially stronger computational evidence than the
earlier shorter scans, while still not replacing proof.

------------------------------------------------------------------------

## 15. False-Tail Detection and Stress Testing

One earlier shorter computation for

\[ k=80 \]

suggested a candidate preperiod near

\[ 99{,}685. \]

After increasing the computational horizon to

\[ N=500{,}000, \]

the candidate changed to

\[ `\boxed{ \text{preperiod}=0,\qquad p=947. }`{=tex} \]

The observed residues were

\[ {0,86,168,249,785,866}`\pmod{947}`{=tex}. \]

This is an important methodological example: a finite sequence can
contain a long tail that appears periodic without representing the true
eventual behavior.

Therefore the project distinguishes between:

1.  finite computational observations;
2.  conjectured eventual behavior;
3.  mathematically proved behavior.

The (k=80) correction is retained as evidence for why deeper stress
testing is necessary.

------------------------------------------------------------------------

## 16. Other Notable Deep-Scan Observations

The (N=500{,}000) scan also produced several large or irregular
candidate periods.

Examples include:

\[ p(80)=947, \]

\[ p(81)=597, \]

and

\[ p(107)=1370. \]

For (k=107),

\[ `\frac{p}{k}`{=tex}=`\frac{1370}{107}`{=tex}`\approx12.80`{=tex}. \]

These cases demonstrate the complexity of the game, but they are not
currently the primary proof targets. Clean parameterized regimes are
considered more useful for theorem discovery than isolated large
periods.

------------------------------------------------------------------------

## 17. Interpretation of the Evidence

The current evidence suggests that (D(k,1)) does not follow one
universal simple period formula.

Instead, (k) appears to pass through distinct structural regimes.

Within some regimes:

-   the period is affine in (k);
-   the number of starting P-residues is fixed;
-   the residues themselves are affine functions of (k).

At regime boundaries, the behavior can change abruptly.

This motivates the working hypothesis:

> **For (m=1), the parameter (k) is partitioned into structural regimes
> in which the period and starting P-position residues admit simple
> affine descriptions.**

This is a hypothesis, not yet a theorem.

------------------------------------------------------------------------

## 18. Current Primary Theorem Candidate

The most attractive current finite-range theorem candidate is:

> For every integer (k) with (58`\le`{=tex}k`\le78`{=tex}), the starting
> P-positions of (D(k,1)) are exactly the integers satisfying
>
> \[ n`\equiv0`{=tex}, 86, k+87`\pmod{2k+88}`{=tex}. \]

The computational evidence through (N=500{,}000) strongly supports this
statement.

However, a proof cannot be obtained from the starting sequence alone.
The proof is expected to require classification of the complete state
((n,s)).

------------------------------------------------------------------------

## 19. Next Phase: Full-State Structural Analysis

The next phase changes the purpose of computation.

Instead of scanning larger (k), Python will be used to examine

\[ g(n,s)=0 \]

throughout the complete state space.

For each selected (k), define

\[ Z\_{k,s} = {n`\bmod`{=tex}p:g(n,s)=0}, \]

where (p) is the observed starting period.

The analysis will:

1.  compute the full SG table;
2.  extract every zero-SG state ((n,s));
3.  reduce (n) modulo the candidate period;
4.  compare the zero-state residue sets across (s);
5.  search for affine boundaries and formulas involving (s) and (k);
6.  compare the same normalized structure across several (k)-values in
    the (58`\le`{=tex}k`\le78`{=tex}) regime;
7.  formulate a candidate complete description of the P-states.

The most useful outcome would be a compact description of a set

\[ `\mathcal`{=tex}P_k =
{(n,s):`\text{specified modular and inequality conditions}`{=tex}}. \]

------------------------------------------------------------------------

## 20. Planned Proof Strategy

Once a candidate full-state description (`\mathcal`{=tex}P_k) is
identified, the intended proof method is the standard P/N
characterization.

### Condition 1: No P-to-P move

Show that if

\[ (n,s)`\in`{=tex}`\mathcal`{=tex}P_k, \]

then no legal move (r) satisfying

\[ \|r-s\|\>1 \]

produces another state in (`\mathcal`{=tex}P_k).

### Condition 2: Every N-state reaches P

Show that every state outside (`\mathcal`{=tex}P_k) has at least one
legal removal (r) such that

\[ (n-r,r)`\in`{=tex}`\mathcal`{=tex}P_k. \]

If both conditions hold, (`\mathcal`{=tex}P_k) is exactly the set of
P-positions.

The unrestricted starting-position theorem can then be derived from the
legal first moves into these classified states.

------------------------------------------------------------------------

## 21. Stronger Long-Term Target

If the two observed affine regimes arise from the same mechanism, the
stronger target is a family indexed by a parameter (t).

The desired type of result would be:

\[ L_t`\le`{=tex}k`\le`{=tex}U_t \]

implies

\[ p_t(k)=2k+A_t+2 \]

and

\[ P_k `\equiv`{=tex} {0,A_t,k+A_t+1} `\pmod{p_t(k)}`{=tex}. \]

The main unanswered questions are:

-   What determines (A_t)?
-   What determines the regime boundaries (L_t,U_t)?
-   Why do the observed values (54) and (86) occur?
-   Is there an infinite sequence of such regimes?
-   Why do simple (p=k+1) blocks reappear between more complex regimes?

These questions will only be promoted to formal conjectures when
additional structural evidence is available.

------------------------------------------------------------------------

## 22. Reproducibility and Research Records

For each computational experiment, the following should be retained:

-   source-code version;
-   programming language and compiler/interpreter version;
-   exact command or parameters;
-   values of (m), (k), and (N);
-   maximum searched period;
-   raw CSV output;
-   generated report;
-   date of run;
-   whether the result is exploratory, deeply validated, or proved;
-   any later run that contradicts or modifies an earlier
    interpretation.

The slow reference solver and automated self-tests should remain part of
the codebase.

------------------------------------------------------------------------

## 23. Current Status Summary

### Established computationally within tested ranges

-   The recurrence and solver have been independently cross-checked on
    small cases.
-   (m=0,1,2) have been compared computationally.
-   (m=1) displays distinct structural regimes.
-   The (42`\le`{=tex}k`\le52`{=tex}) affine pattern survived deep
    testing to (N=500{,}000).
-   The (58`\le`{=tex}k`\le78`{=tex}) affine pattern survived deep
    testing to (N=500{,}000).
-   Deep testing corrected an earlier misleading finite-tail
    interpretation at (k=80).

### Not yet proved

-   Eventual periodicity for the observed (m=1) regimes in general.
-   The exact infinite P-position formulas for
    (42`\le`{=tex}k`\le52`{=tex}) and (58`\le`{=tex}k`\le78`{=tex}).
-   A general rule generating the constants (54,86,`\ldots`{=tex}).
-   A formula for the boundaries of the affine regimes.
-   An infinite family of affine regimes.

### Immediate research objective

**Determine the complete zero-SG state structure ((n,s)) for the
(58`\le`{=tex}k`\le78`{=tex}) regime and use it to formulate a
proof-ready classification theorem.**

------------------------------------------------------------------------

## 24. Research Principle Going Forward

The computational program is being used to:

\[ `\text{discover patterns}`{=tex} `\rightarrow`{=tex}
`\text{stress-test them}`{=tex} `\rightarrow`{=tex}
`\text{find counterexamples}`{=tex} `\rightarrow`{=tex}
`\text{formulate conjectures}`{=tex}. \]

The next stage is to convert those conjectures into mathematical
statements that can be proved directly from the rules of the game.

Large computations are therefore not the final result; they are the
experimental tool used to discover the underlying combinatorial
structure. ---

## 25. First Result from the Full-State Python Phase

After the methodology above was established, the next proof-oriented
computation was performed in Python.

For (m=1), define the **winning-move set**

\[ A_n =
{r`\in`{=tex}{1,`\ldots`{=tex},`\min`{=tex}(k,n)}:(n-r,r)`\text{ is a P-state}`{=tex}}.
\]

This gives an exact Boolean reformulation of the game.

The unrestricted starting position at heap size (n) is P exactly when

\[ `\boxed{A_n=\varnothing.}`{=tex} \]

For a state with previous move (s), the only forbidden next removals are

\[ {s-1,s,s+1} \]

after clipping to ({1,`\ldots`{=tex},k}). Therefore,

\[ `\boxed{
(n,s)\text{ is P}
\iff
A_n\subseteq\{s-1,s,s+1\}.
}`{=tex} \]

This identity follows directly from the P/N recurrence: a state is P
precisely when every move that would reach a P-state is forbidden.

This reformulation is useful because the proof search no longer needs
arbitrary SG values. It can work with Boolean P/N rows and the sets
(A_n).

------------------------------------------------------------------------

## 26. Independent Boolean Solver

A second Python solver was implemented using only P/N information.

For each (n):

1.  It forms (A_n) by checking which removals (r) lead to a previously
    computed P-state ((n-r,r)).
2.  It declares the unrestricted start at (n) P iff (A_n) is empty.
3.  For each previous move (s), it declares ((n,s)) P iff every member
    of (A_n) lies inside the forbidden interval (\[s-1,s+1\]).

This Boolean solver does not calculate mex or nonzero SG values.

Its complete P/N output was compared against the original SG solver for
the tested (58`\le `{=tex}k`\le78`{=tex}) cases, and the two methods
agreed on both:

-   unrestricted starting P/N positions;
-   every full state ((n,s)) checked.

This provides a second implementation of the part of the recurrence
relevant to P-position classification.

------------------------------------------------------------------------

## 27. Exact Finite-State Period Certificate

The Boolean recurrence has finite memory.

To compute row (n), the game only needs states of the form

\[ (n-r,r), `\qquad
1`{=tex}`\le `{=tex}r`\le `{=tex}k. \]

Therefore row (n) depends only on the preceding (k) rows.

Let (R_n) denote the complete Boolean P/N row

\[ R_n= (P(n,1),P(n,2),`\ldots`{=tex},P(n,k)). \]

Suppose that for some offset (t) and candidate period (p),

\[ R\_{t+i}=R\_{t+p+i} \]

for every

\[ 0`\le `{=tex}i\<k. \]

Then the next rows must also agree:

\[ R\_{t+k}=R\_{t+p+k}, \]

because they are computed from identical preceding (k)-row states.

Repeating this argument inductively proves

\[ `\boxed{
R_n=R_{n+p}\quad\text{for every }n\ge t.
}`{=tex} \]

Thus equality of two (k)-row state windows is an **exact finite
certificate of future P/N periodicity**, rather than a finite-tail
heuristic.

------------------------------------------------------------------------

## 28. Certificate Results for the (58`\le `{=tex}k`\le78`{=tex}) Regime

The Python Boolean solver was used to test the candidate period

\[ p=2k+88 \]

for every integer

\[ 58`\le `{=tex}k`\le78`{=tex}. \]

For every one of the 21 parameter values, an exact repeated (k)-row P/N
state window was found.

For

\[ 65`\le `{=tex}k`\le78`{=tex}, \]

the full Boolean state pattern repeats with period (2k+88) beginning at

\[ t=0. \]

For

\[ 58`\le `{=tex}k`\le64`{=tex}, \]

the full Boolean state pattern has a short transient, with the
certificate beginning near (t=58) or (59).

Despite that short full-state transient, the unrestricted starting
P-position sequence was separately checked through a finite prefix long
enough to cover one complete starting-position period after the
full-state cycle becomes active. For a cycle beginning at `t`, the
verification bound used by the standalone verifier is `t + k + p - 1`. For every

\[ 58`\le `{=tex}k`\le78`{=tex}, \]

the starting sequence is thereby exactly certified to have period

\[ `\boxed{2k+88}`{=tex} \]

from (n=0), with residues

\[ `\boxed{
\{0,86,k+87\}.
}`{=tex} \]

This is stronger than observing the same pattern through (N=500{,}000):
for each of these 21 fixed values of (k), the finite-state recurrence
supplies a certificate that forces the P/N pattern to continue
indefinitely.

This remains a **computer-assisted finite-range certification**, not yet
a symbolic human proof explaining simultaneously why every (k) in the
interval has this form or why the interval boundaries are (58) and (78).

------------------------------------------------------------------------

## 29. Updated Immediate Objective

The project now has two complementary goals.

### Exact finite-range result

Preserve and independently verify the Boolean cycle certificates for all

\[ 58`\le `{=tex}k`\le78`{=tex}. \]

A small standalone verifier should eventually be produced so that the
certificate logic can be inspected independently of the exploratory
code.

### Symbolic mathematical result

Use the winning-move sets (A_n) to explain why

\[ p=2k+88 \]

and

\[ P_k`\equiv`{=tex}{0,86,k+87}`\pmod{2k+88}`{=tex} \]

arise, and why the same structure holds exactly over the observed
parameter regime.

The next pattern-mining target is therefore not the SG values
themselves, but the structure of the sets (A_n), especially the residues
for which (A_n) is empty or is contained in three consecutive move
sizes.
