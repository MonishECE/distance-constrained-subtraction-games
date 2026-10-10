# Reproducibility Guide

## Environment

The main scanner is C++17. The original research engine and the
independent full-state verifier are Python.

Recommended:

``` text
Python 3.10+
g++ with C++17 support
```

Optional plotting uses `numpy` and `matplotlib`.

## C++ self-test

From the repository root:

``` bash
g++ -std=c++17 -O3 -DNDEBUG -Wall -Wextra -pedantic \
  src/distance_subtraction_research.cpp \
  -o distance_subtraction_research

./distance_subtraction_research self-test
```

Expected result:

``` text
All self-tests passed.
```

## Representative C++ check

``` bash
./distance_subtraction_research single \
  --k 5 --m 1 --n 2000 \
  --max-period 200 --min-repeats 12 \
  --exact-state-cycle --exact-cycle-max-n 2000
```

The previously verified result is candidate starting period (6), residue
({0}), with an exact full-state cycle of period 6.

## Deep scan

The principal deep scan was:

``` bash
./distance_subtraction_research scan \
  --m-values 1 \
  --k-min 35 \
  --k-max 120 \
  --n 500000 \
  --max-period 150000 \
  --out m1_deep
```

In the original execution environment this was split into two ranges
because of a per-command runtime limit:

``` bash
./distance_subtraction_research scan \
  --m-values 1 --k-min 35 --k-max 80 \
  --n 500000 --max-period 150000 \
  --out m1_deep_35_80

./distance_subtraction_research scan \
  --m-values 1 --k-min 81 --k-max 120 \
  --n 500000 --max-period 150000 \
  --out m1_deep_81_120
```

The merged CSV is preserved at `data/deep_scan/m1_deep_35_120.csv`.

## Independent full-state certificates

Run:

``` bash
python src/full_state_analysis.py certificates \
  --k-min 58 --k-max 78 \
  --out data/certificates/full_state_period_certificates_k58_78.csv
```

The verifier:

1.  Computes the Boolean P/N recurrence.
2.  Finds the earliest repeated (k)-row full-state window separated by
    (p=2k+88).
3.  Uses finite-memory determinism to certify future P/N periodicity.
4.  Checks the claimed starting-position residue formula through
    (t+k+p-1).
5.  Independently recomputes the finite certificate range using a direct
    SG recurrence and requires the P/N states to agree.

## Figure

``` bash
python -m pip install -r requirements.txt

python src/full_state_analysis.py plot \
  --k 68 \
  --out figures/full_state_k68_p_positions.png
```

## Data integrity notes

The certificate CSV in `data/certificates/` is the corrected current
version.

An earlier CSV used the label `finite_prefix_check_through_n` for a
shorter diagnostic bound. During repository assembly, this metadata
field was audited and corrected to the stronger verification bound

\[ t+k+p-1. \]

This correction changes no cycle start, period, residue set, or SG
cross-check result.

Older logs/reports are preserved for historical traceability and should
not override `DISCOVERIES.md` or the corrected certificate CSV.
