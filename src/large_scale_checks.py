#!/usr/bin/env python3
"""Large-scale checks: universal recursion, closed-form runs, template to 1e7.

1. Verify the universal row-nonemptiness recursion against the exact solver
   at k = n = 20000.
2. Generate the recursion sequence to 1e7 and check the closed-form run
   formulas exactly (starts, lengths, gaps).
3. Verify every certified regime template to n = 1e7 at its boundary k's.
"""
from __future__ import annotations

import json
import sys
from array import array
from pathlib import Path

sys.path.insert(0, 'src')
from fast_solver import fast_interval_solver

N_UNIVERSAL = 20_000
N_RUNS = 10_000_000
N_TEMPLATE = 10_000_000

REGIMES = [
    (14, 11, 11), (22, 17, 17), (54, 42, 53), (86, 58, 78),
    (214, 170, 213), (342, 234, 313), (854, 682, 853),
    (1366, 938, 1251), (3414, 2730, 3413), (5462, 3754, 5007),
]
COLLAPSE_ONLY = [(6, 5), (8, 7), (30, 29), (118, 117), (470, 469), (1878, 1877)]


def universal_recursion(limit):
    rows, _ = fast_interval_solver(64, 1, 64)
    a = bytearray(limit + 1)
    for n in range(10):
        a[n] = 1 if rows[n] else 0
    for n in range(10, limit + 1):
        m = n >> 1
        if n & 1:
            a[n] = 1 - (a[m] | a[m + 1])
        else:
            a[n] = 1 - a[m]
    return a


def verify_recursion_vs_solver():
    rows, _ = fast_interval_solver(N_UNIVERSAL, 1, N_UNIVERSAL)
    a = universal_recursion(N_UNIVERSAL)
    for n in range(N_UNIVERSAL + 1):
        assert a[n] == (1 if rows[n] else 0), ('recursion mismatch', n)
    return N_UNIVERSAL


def alive_runs(a, limit):
    runs = []
    val, start = a[0], 0
    for n in range(1, limit + 1):
        if a[n] != val:
            runs.append((val, start, n - 1))
            val, start = a[n], n
    runs.append((val, start, limit))
    return runs


def closed_form_starts(limit):
    starts = [0, 6, 8]
    j = 3
    while True:
        p = 1 << j
        g = (2 + 5 * p) // 3
        if g > limit:
            break
        for x in (g, g + p, g + 2 * p):
            if x <= limit:
                starts.append(x)
        j += 2
    return sorted(starts)


def closed_form_lengths(limit):
    lens = {0: 5, 6: 1, 8: 3}
    gaps = {4: 1, 6: 1, 10: 3}
    j = 3
    while True:
        p = 1 << j
        g = (2 + 5 * p) // 3
        if g > limit:
            break
        lens[g] = (p // 2 - 1) // 3
        lens[g + p] = (2 * p - 1) // 3
        lens[g + 2 * p] = (5 * p - 1) // 3
        gaps[g + lens[g] - 1] = (5 * p // 2 + 1) // 3
        gaps[g + p + lens[g + p] - 1] = (p + 1) // 3
        gaps[g + 2 * p + lens[g + 2 * p] - 1] = (4 * p + 1) // 3
        j += 2
    return lens, gaps


def verify_runs():
    a = universal_recursion(N_RUNS)
    runs = alive_runs(a, N_RUNS)
    starts = [s for v, s, e in runs if v == 1]
    cf = closed_form_starts(N_RUNS)
    assert starts == cf, ('start mismatch', len(starts), len(cf))
    lens, gaps = closed_form_lengths(N_RUNS)
    for v, s, e in runs:
        if e == N_RUNS:
            continue
        L = e - s + 1
        if v == 1:
            assert lens.get(s) == L, ('length mismatch', s, L, lens.get(s))
        else:
            assert gaps.get(s - 1) == L, ('gap mismatch', s - 1, L, gaps.get(s - 1))
    return {'limit': N_RUNS, 'alive_runs': len(starts),
            'last_start': starts[-1], 'formula_ok': True}


def template_first_mismatch_large(k, A, N):
    p = 2 * k + A + 2
    r2, r3 = A % p, (k + A + 1) % p
    size = N + k + 2
    maxA = array('i', [0]) * size
    minA = array('i', [0]) * size
    cnt = array('i', [0]) * size
    for n in range(N + 1):
        t = n % p
        pred = (t == 0) or (t == r2) or (t == r3)
        if cnt[n] == 0:
            if not pred:
                return n
            end = min(k, N - n)
            for r in range(1, end + 1):
                tt = n + r
                if cnt[tt] == 0 or r < minA[tt]:
                    minA[tt] = r
                if r > maxA[tt]:
                    maxA[tt] = r
                cnt[tt] += 1
        else:
            if pred:
                return n
            lo = max(1, maxA[n] - 1)
            hi = min(k, minA[n] + 1)
            if lo <= hi:
                end = min(hi, N - n)
                for r in range(lo, end + 1):
                    tt = n + r
                    if cnt[tt] == 0 or r < minA[tt]:
                        minA[tt] = r
                    if r > maxA[tt]:
                        maxA[tt] = r
                    cnt[tt] += 1
    return None


def main():
    base = Path('data/certificates')
    out = {}
    out['universal_recursion_through'] = verify_recursion_vs_solver()
    print('universal recursion verified against solver through',
          out['universal_recursion_through'], flush=True)
    out['runs'] = verify_runs()
    print('closed-form runs verified:', out['runs'], flush=True)
    checks = []
    for A, lo, hi in REGIMES:
        for k in sorted({lo, hi}):
            bad = template_first_mismatch_large(k, A, N_TEMPLATE)
            assert bad is None, (A, k, 'template break', bad)
            checks.append({'A': A, 'k': k, 'n_max': N_TEMPLATE})
            print(f'  template A={A} k={k} holds through {N_TEMPLATE}', flush=True)
    for A, k in COLLAPSE_ONLY:
        bad = template_first_mismatch_large(k, A, N_TEMPLATE)
        assert bad is None, (A, k, 'collapse break', bad)
        checks.append({'A': A, 'k': k, 'n_max': N_TEMPLATE, 'collapse': True})
        print(f'  collapse A={A} k={k} holds through {N_TEMPLATE}', flush=True)
    out['template_checks'] = checks
    out['all_passed'] = True
    (base / 'large_scale_checks.json').write_text(
        json.dumps(out, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'all_passed': True, 'template_checks': len(checks)}, indent=2))


if __name__ == '__main__':
    main()
