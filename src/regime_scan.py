#!/usr/bin/env python3
"""Large-scale affine-template scan for D(k,1).

For each k, compute the exact start P/N sequence once, then test every
candidate template

    T(k,A):  P(n) <=> n mod p in {0, A, k+A+1},  p = 2k+A+2

over the whole computed range with early exit. Also records the minimal
eventual period found by a suffix-period detector.

Standard library only; exact integer arithmetic.
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'methodology/theorem_B'))
from verify_theorems_ab import interval_solver


def minimal_suffix_period(seq: bytes, max_period: int, min_repeats: int = 12):
    """Minimal p such that the last min_repeats*p symbols repeat with period p.

    Returns (p, preperiod) or None. The long repeat window suppresses
    spurious tiny periods from short constant tails.
    """
    L = len(seq)
    for p in range(1, max_period + 1):
        need = min_repeats * p
        if need > L:
            break
        tail = seq[L - need:]
        ok = True
        for j in range(1, min_repeats):
            if tail[(j - 1) * p:j * p] != tail[j * p:(j + 1) * p]:
                ok = False
                break
        if not ok:
            continue
        last = -1
        for i in range(L - p):
            if seq[i] != seq[i + p]:
                last = i
        return p, last + 1
    return None


def template_matches(seq: bytes, k: int, A: int, through: int) -> int | None:
    """First n <= through where T(k,A) fails, or None if it holds throughout."""
    p = 2 * k + A + 2
    r1, r2, r3 = 0, A % p, (k + A + 1) % p
    end = min(through, len(seq) - 1)
    for n in range(end + 1):
        pred = (n % p == r1) or (n % p == r2) or (n % p == r3)
        if seq[n] != (1 if pred else 0):
            return n
    return None


def scan_one(k: int, nmul: int, base: int, amax_extra: int = 60):
    n_max = nmul * k + base
    rows, starts = interval_solver(k, 1, n_max)
    seq = bytes(1 if x else 0 for x in starts)
    det = minimal_suffix_period(seq, max_period=10 * k + 400)
    minp, pre = (det if det else (None, None))

    matches = []
    first_fail = {}
    for A in range(k + 1, 2 * k + amax_extra + 1):
        f = template_matches(seq, k, A, n_max)
        if f is None:
            matches.append(A)
        elif f >= n_max - 2 * (2 * k + A + 2):
            # failed only near the end: record as "late failure" for boundary study
            first_fail[A] = f
    return dict(k=k, n_max=n_max, min_period=minp, preperiod=pre,
                template_A=(";".join(map(str, matches)) if matches else ""),
                late_failures=(";".join(f"{a}@{n}" for a, n in sorted(first_fail.items())) if first_fail else ""))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k-min", type=int, default=2)
    ap.add_argument("--k-max", type=int, default=250)
    ap.add_argument("--nmul", type=int, default=26)
    ap.add_argument("--base", type=int, default=600)
    ap.add_argument("--amax-extra", type=int, default=60)
    ap.add_argument("--out", type=Path, default=Path("data/regimes/template_scan.csv"))
    args = ap.parse_args()

    records = []
    for k in range(args.k_min, args.k_max + 1):
        rec = scan_one(k, args.nmul, args.base, args.amax_extra)
        records.append(rec)
        tag = f"A={rec['template_A']}" if rec["template_A"] else "no-template"
        print(f"k={k:4d} minp={str(rec['min_period']):>6} pre={str(rec['preperiod']):>4} {tag}"
              + (f"  late={rec['late_failures']}" if rec['late_failures'] else ""), flush=True)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(records[0]))
        w.writeheader()
        w.writerows(records)

    print("\n=== template A-values by k ===")
    for r in records:
        if r["template_A"]:
            print(f"k={r['k']}: A={r['template_A']}")
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
