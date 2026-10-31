#!/usr/bin/env python3
"""Targeted scans of universal 1-run starts for further genuine regimes.

For each tested (A, k) the template T(k,A) is falsified by finding an explicit
first n where the predicted and actual starting outcomes differ.  The genuine
ranges are certified separately by verify_hierarchy.py; these scans cover the
remaining k values and provide the negative evidence quoted in Theorem C.

Output: data/certificates/targeted_scans.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

sys.path.insert(0, 'src')
from fast_solver import fast_interval_solver

# (A, k_first, k_last, step, note)
SCANS = [
    (1366, 342, 937, 1, 'below the certified genuine interval'),
    (1366, 1252, 1365, 1, 'above the certified genuine interval'),
    (1878, 470, 1876, 1, 'all k below the collapse-only k=A-1'),
    (7510, 3754, 7508, 125, 'coarse scan of the plausible range'),
]


def targets(k, A, n, p):
    t = n % p
    return t == 0 or t == A or t == k + A + 1


def first_failure(k, A):
    p = 2 * k + A + 2
    limit = 6 * p + 4 * k + 20
    rows, starts = fast_interval_solver(k, 1, limit)
    for n in range(limit + 1):
        if starts[n] != targets(k, A, n, p):
            return n, p
    return None, p


def main():
    out = []
    for A, lo, hi, step, note in SCANS:
        t0 = time.time()
        tested = 0
        worst = (0, None)
        for k in range(lo, hi + 1, step):
            if k >= A:
                continue
            n, p = first_failure(k, A)
            assert n is not None, (A, k, 'no counterexample: possible genuine regime')
            tested += 1
            if n > worst[0]:
                worst = (n, k)
        rec = {'A': A, 'k_first': lo, 'k_last': hi, 'step': step,
               'tested': tested, 'largest_first_failure_n': worst[0],
               'at_k': worst[1], 'seconds': round(time.time() - t0, 1),
               'note': note}
        out.append(rec)
        print(json.dumps(rec), flush=True)
    path = Path('data/certificates/targeted_scans.json')
    path.write_text(json.dumps({'scans': out, 'all_failed_as_expected': True},
                               indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'all_failed_as_expected': True, 'scans': len(out)}, indent=2))


if __name__ == '__main__':
    main()
