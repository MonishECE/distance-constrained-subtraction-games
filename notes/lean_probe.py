#!/usr/bin/env python3
"""Streaming upper-endpoint probe for the m=1 regime template.

compact_probe.py stores full row and start arrays. At j=23 those arrays are
large enough to matter, so this script streams the recurrence and checks the
three certificate conditions on the fly. It keeps only:

  * min_a, max_a: the least and greatest legal subtraction seen so far for
    each future heap size;
  * first_k: the first k rows, needed for the repeated-window check.

The recurrence and certificate conditions are identical to the upper mode of
compact_probe.py:

  * rows[0:k] == rows[p:p+k]                    (repeated window at t=0)
  * starts[n] == [n mod p in {0,A,k+A+1}]       (template through the bridge)
  * starts[n] == starts[n mod p]                (least period)

Example:
    python notes/lean_probe.py --k 20505487 --A 22369622
    python notes/lean_probe.py --k 20505488 --A 22369622 --mode upper-fail
"""
from __future__ import annotations

import argparse
import time
from array import array


def check_upper(k: int, a: int) -> dict:
    p = 2 * k + a + 2
    bridge = k + p - 1
    size = bridge + 1
    min_a = array("i", [0]) * size
    max_a = array("i", [0]) * size
    first_k = array("i", [0]) * k

    window_bad = None
    template_bad = None
    least_bad = None
    t0 = time.time()

    for n in range(size):
        if min_a[n] == 0:
            row = 1
            end = min(k, bridge - n)
            for r in range(1, end + 1):
                t = n + r
                if min_a[t] == 0 or r < min_a[t]:
                    min_a[t] = r
                if r > max_a[t]:
                    max_a[t] = r
        else:
            lo = max(1, max_a[n] - 1)
            hi = min(k, min_a[n] + 1)
            if lo <= hi:
                row = 4 * lo + (hi - lo)
                end = min(hi, bridge - n)
                for r in range(lo, end + 1):
                    t = n + r
                    if min_a[t] == 0 or r < min_a[t]:
                        min_a[t] = r
                    if r > max_a[t]:
                        max_a[t] = r
            else:
                row = 0

        if n < k:
            first_k[n] = row

        if template_bad is None:
            t = n % p
            expected = t == 0 or t == a or t == k + a + 1
            if expected != (min_a[n] == 0):
                template_bad = n

        if least_bad is None and n >= p:
            if (min_a[n] == 0) != (min_a[n % p] == 0):
                least_bad = n

        if window_bad is None and p <= n < p + k:
            if row != first_k[n - p]:
                window_bad = n

        if n and n % (1 << 24) == 0:
            print(f"n={n} elapsed={time.time() - t0:.1f}s", flush=True)

    return {
        "mode": "upper",
        "k": k,
        "A": a,
        "period": p,
        "bridge": bridge,
        "window_ok": window_bad is None,
        "window_first_bad": window_bad,
        "template_ok": template_bad is None,
        "template_first_bad": template_bad,
        "least_period_ok": least_bad is None,
        "least_period_first_bad": least_bad,
        "seconds": round(time.time() - t0, 2),
    }


def check_upper_failure(k: int, a: int) -> dict:
    """Find the first template mismatch for a parameter just above K_j."""
    p = 2 * k + a + 2
    upto = p + a
    size = upto + 1
    min_a = array("i", [0]) * size
    max_a = array("i", [0]) * size
    first_bad = None
    t0 = time.time()

    for n in range(size):
        if min_a[n] == 0:
            start = True
            end = min(k, upto - n)
            for r in range(1, end + 1):
                t = n + r
                if min_a[t] == 0 or r < min_a[t]:
                    min_a[t] = r
                if r > max_a[t]:
                    max_a[t] = r
        else:
            start = False
            lo = max(1, max_a[n] - 1)
            hi = min(k, min_a[n] + 1)
            if lo <= hi:
                end = min(hi, upto - n)
                for r in range(lo, end + 1):
                    t = n + r
                    if min_a[t] == 0 or r < min_a[t]:
                        min_a[t] = r
                    if r > max_a[t]:
                        max_a[t] = r

        if first_bad is None:
            t = n % p
            expected = t == 0 or t == a or t == k + a + 1
            if expected != start:
                first_bad = n

        if n and n % (1 << 24) == 0:
            print(f"n={n} elapsed={time.time() - t0:.1f}s", flush=True)

    return {
        "mode": "upper-fail",
        "k": k,
        "A": a,
        "period": p,
        "upto": upto,
        "expected_first_bad": p + a,
        "first_bad": first_bad,
        "seconds": round(time.time() - t0, 2),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--A", type=int, required=True)
    ap.add_argument("--mode", choices=("upper", "upper-fail"), default="upper")
    args = ap.parse_args()
    if args.mode == "upper":
        print(check_upper(args.k, args.A))
    else:
        print(check_upper_failure(args.k, args.A))


if __name__ == "__main__":
    main()
