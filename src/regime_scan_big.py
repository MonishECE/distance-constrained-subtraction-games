#!/usr/bin/env python3
"""Large-scale affine-template scan for D(k,1) using the fast event solver.

Tests T(k,A): P(n) <=> n mod (2k+A+2) in {0, A, k+A+1}
for every k and every candidate A, over a long exact prefix. Distinguishes
genuine three-residue regimes (A != k+1) from arithmetic collapse cases.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

from fast_solver import fast_interval_solver


def template_first_failure(starts, k, A, through):
    p = 2 * k + A + 2
    r2, r3 = A % p, (k + A + 1) % p
    end = min(through, len(starts) - 1)
    for n in range(end + 1):
        t = n % p
        pred = (t == 0) or (t == r2) or (t == r3)
        if starts[n] != pred:
            return n
    return None


def scan_one(k, nmul, base, amax_extra):
    n_max = nmul * k + base
    _, starts = fast_interval_solver(k, 1, n_max)
    genuine = []
    collapse = False
    late = {}
    for A in range(k + 1, 2 * k + amax_extra + 1):
        f = template_first_failure(starts, k, A, n_max)
        if f is None:
            if A == k + 1:
                collapse = True
            else:
                genuine.append(A)
        elif f >= n_max - 2 * (2 * k + A + 2):
            late[A] = f
    return dict(k=k, n_max=n_max, genuine=genuine, collapse=collapse, late=late)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--k-min", type=int, default=2)
    ap.add_argument("--k-max", type=int, default=600)
    ap.add_argument("--nmul", type=int, default=30)
    ap.add_argument("--base", type=int, default=2000)
    ap.add_argument("--amax-extra", type=int, default=60)
    ap.add_argument("--out", type=Path, default=Path("data/regimes/template_scan_big.csv"))
    args = ap.parse_args()

    records = []
    for k in range(args.k_min, args.k_max + 1):
        rec = scan_one(k, args.nmul, args.base, args.amax_extra)
        records.append(rec)
        if rec["genuine"] or rec["late"]:
            print(f"k={k:4d} genuine={rec['genuine']} late={rec['late']}", flush=True)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["k", "n_max", "genuine", "collapse", "late"])
        w.writeheader()
        for r in records:
            w.writerow({"k": r["k"], "n_max": r["n_max"],
                        "genuine": ";".join(map(str, r["genuine"])),
                        "collapse": r["collapse"],
                        "late": ";".join(f"{a}@{n}" for a, n in sorted(r["late"].items()))})

    print("\n=== genuine three-residue regimes ===")
    for r in records:
        if r["genuine"]:
            print(f"k={r['k']}: A={r['genuine']}")
    print(f"\nWrote {args.out}")


if __name__ == "__main__":
    main()
