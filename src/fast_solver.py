#!/usr/bin/env python3
"""Fast event-driven interval solver for D(k,m) and regime exploration.

Key idea: every non-full row Q_m is an interval of at most 2m+1 values.
Row m attacks heap n = m+r with move r for each r in Q_m.  Instead of
recomputing A_n by scanning k predecessors, register each attack as an
event on the target heap.  Total work is O(n_max) plus O(k) per full row,
and full rows occur with density O(1/k), so the whole solve is O(n_max).

Exact integer arithmetic; no external packages.
"""
from __future__ import annotations

import argparse
import sys


def fast_interval_solver(k: int, m: int, upto: int):
    """Return (rows, starts) with rows[n] the bitmask of P-states (n,s).

    Semantics identical to verify_theorems_ab.interval_solver.
    """
    if k < 1 or m < 0 or upto < 0:
        raise ValueError("Require k>=1, m>=0, upto>=0")
    full = (1 << k) - 1
    size = upto + k + 2
    maxA = [0] * size
    minA = [0] * size
    cnt = [0] * size
    rows = [0] * (upto + 1)
    starts = [False] * (upto + 1)

    for n in range(upto + 1):
        if cnt[n] == 0:
            starts[n] = True
            rows[n] = full
            # register all moves 1..k on heaps n+1 .. n+k
            end = min(k, upto - n)
            for r in range(1, end + 1):
                t = n + r
                if cnt[t] == 0 or r < minA[t]:
                    minA[t] = r
                if r > maxA[t]:
                    maxA[t] = r
                cnt[t] += 1
        else:
            starts[n] = False
            lo = max(1, maxA[n] - m)
            hi = min(k, minA[n] + m)
            if lo <= hi:
                mask = ((1 << (hi - lo + 1)) - 1) << (lo - 1)
                rows[n] = mask
                end = min(hi, upto - n)
                for r in range(lo, end + 1):
                    t = n + r
                    if cnt[t] == 0 or r < minA[t]:
                        minA[t] = r
                    if r > maxA[t]:
                        maxA[t] = r
                    cnt[t] += 1
            else:
                rows[n] = 0
    return rows, starts


def crosscheck(kmax: int = 60, nmax: int = 120, mmax: int = 4) -> int:
    from verify_theorems_ab import interval_solver, naive_solver
    checks = 0
    for k in range(1, kmax + 1):
        for m in range(0, mmax + 1):
            fast = fast_interval_solver(k, m, nmax)
            ref = interval_solver(k, m, nmax)
            assert fast == ref, ("fast/ref mismatch", k, m)
            if k <= 12:
                assert fast == naive_solver(k, m, nmax), ("naive mismatch", k, m)
            checks += 1
    return checks


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--crosscheck", action="store_true")
    ap.add_argument("--bench", type=int, default=0)
    args = ap.parse_args()
    if args.crosscheck:
        print(f"crosschecks passed: {crosscheck()}")
    if args.bench:
        import time
        t0 = time.time()
        rows, starts = fast_interval_solver(args.bench, 1, 50 * args.bench + 1000)
        dt = time.time() - t0
        print(f"k={args.bench} n={len(rows)-1} time={dt:.2f}s")
