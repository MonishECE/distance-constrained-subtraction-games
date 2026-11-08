#!/usr/bin/env python3
"""Memory-lean endpoint probe for the m=1 regime template.

The repository's fast_interval_solver stores full rows as Python bitmasks.
That is fine for the published ranges, but at j=19 and beyond the bitmask
arrays can exhaust memory. For m=1 every non-full row has at most three
entries, so this script encodes each row as a small integer:

    0                 empty row
    1                 full row
    4*lo + (hi-lo)    interval [lo,hi], with hi-lo <= 2

The recurrence is identical to fast_interval_solver. The script is a
standalone probe; it does not write any repository data.

Examples:
    python notes/compact_probe.py --k 320399 --A 349526 --mode upper
    python notes/compact_probe.py --k 961194 --A 1398102 --mode lower
"""
from __future__ import annotations

import argparse
import sys
import time
from array import array
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from verify_hierarchy import find_window  # noqa: E402


def solve(k: int, upto: int):
    """Return (rows, starts) using the compact m=1 row encoding."""
    size = upto + k + 2
    min_a = array("i", [0]) * size
    max_a = array("i", [0]) * size
    cnt = array("i", [0]) * size
    rows = array("i", [0]) * (upto + 1)
    starts = bytearray(upto + 1)

    for n in range(upto + 1):
        if cnt[n] == 0:
            starts[n] = 1
            rows[n] = 1
            end = min(k, upto - n)
            for r in range(1, end + 1):
                t = n + r
                if cnt[t] == 0 or r < min_a[t]:
                    min_a[t] = r
                if r > max_a[t]:
                    max_a[t] = r
                cnt[t] += 1
        else:
            lo = max(1, max_a[n] - 1)
            hi = min(k, min_a[n] + 1)
            if lo <= hi:
                rows[n] = 4 * lo + (hi - lo)
                end = min(hi, upto - n)
                for r in range(lo, end + 1):
                    t = n + r
                    if cnt[t] == 0 or r < min_a[t]:
                        min_a[t] = r
                    if r > max_a[t]:
                        max_a[t] = r
                    cnt[t] += 1
            else:
                rows[n] = 0
    return rows, starts


def targets(n: int, k: int, a: int, p: int) -> bool:
    t = n % p
    return t == 0 or t == a or t == k + a + 1


def check_upper(k: int, a: int) -> dict:
    p = 2 * k + a + 2
    bridge = k + p - 1
    t0 = time.time()
    rows, starts = solve(k, bridge)
    window = rows[0:k] == rows[p:p + k]
    bad = next((n for n in range(bridge + 1) if starts[n] != targets(n, k, a, p)), None)
    least = all(starts[n] == starts[n % p] for n in range(bridge + 1))
    return {
        "mode": "upper", "k": k, "A": a, "period": p, "window_start": 0 if window else None,
        "bridge": bridge, "template_ok": bad is None, "first_bad": bad,
        "least_period_ok": least, "seconds": round(time.time() - t0, 2),
    }


def check_lower(k: int, a: int) -> dict:
    p = 2 * k + a + 2
    upto = 3 * p + k + 10
    t0 = time.time()
    rows, starts = solve(k, upto)
    window = find_window(rows, k, p)
    if window is None:
        return {"mode": "lower", "k": k, "A": a, "period": p, "window_start": None,
                "template_ok": False, "first_bad": None, "least_period_ok": False,
                "seconds": round(time.time() - t0, 2)}
    bridge = window + k + p - 1
    bad = next((n for n in range(bridge + 1) if starts[n] != targets(n, k, a, p)), None)
    least = all(starts[n] == starts[n % p] for n in range(bridge + 1))
    row_ok = all(rows[n] == rows[n + p] for n in range(window, upto - p + 1))
    return {
        "mode": "lower", "k": k, "A": a, "period": p, "window_start": window,
        "bridge": bridge, "template_ok": bad is None, "first_bad": bad,
        "least_period_ok": least, "row_equality_ok": row_ok,
        "seconds": round(time.time() - t0, 2),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--k", type=int, required=True)
    ap.add_argument("--A", type=int, required=True)
    ap.add_argument("--mode", choices=("upper", "lower"), required=True)
    args = ap.parse_args()
    result = check_upper(args.k, args.A) if args.mode == "upper" else check_lower(args.k, args.A)
    print(result)


if __name__ == "__main__":
    main()
