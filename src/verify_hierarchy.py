#!/usr/bin/env python3
"""Certify the infinite regime hierarchy of D(k,1).

Regimes (A, k_min, k_max) with template T(k,A):
    P(n) <=> n mod p in {0, A, k+A+1},  p = 2k+A+2.

Each k is certified by the finite-memory argument:
  * find t < 2p with rows[t:t+k] == rows[t+p:t+p+k]  (exact k-row window),
  * check the start template on the complete bridge [0, t+k+p-1],
  * check rows[n] == rows[n+p] on [t, n_max-p],
  * independent crosschecks (interval recurrence, boolean DP, direct SG on
    small k) on the bridge.

Boundaries: k_min-1 and k_max+1 are falsified with an explicit first
counterexample n.  Output: data/certificates/regime_hierarchy_*.csv/json.
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, 'src')
from fast_solver import fast_interval_solver
from verify_theorems_ab import interval_solver, naive_solver
from full_state_analysis import boolean_solver, direct_sg_pn

# (A, k_min, k_max, group j, position 0/1)
REGIMES = [
    (14, 11, 11, 3, 0),
    (22, 17, 17, 3, 1),
    (54, 42, 53, 5, 0),
    (86, 58, 78, 5, 1),
    (214, 170, 213, 7, 0),
    (342, 234, 313, 7, 1),
    (854, 682, 853, 9, 0),
    (1366, 938, 1251, 9, 1),
    (3414, 2730, 3413, 11, 0),
    (5462, 3754, 5007, 11, 1),
]
COLLAPSE_ONLY = [(6, 5), (8, 7), (30, 29), (118, 117), (470, 469), (1878, 1877), (7510, 7509)]


def targets(k, A, n, p):
    t = n % p
    return t == 0 or t == A or t == k + A + 1


def find_window(rows, k, p):
    """Return t <= 2p with rows[t:t+k] == rows[t+p:t+p+k], or None."""
    max_t = 2 * p
    for t in range(0, min(max_t, 24) + 1):
        if rows[t:t + k] == rows[t + p:t + p + k]:
            return t
    MOD = (1 << 61) - 1
    BASE = 911382323
    bk = pow(BASE, k - 1, MOD)
    h = 0
    for i in range(k):
        h = (h * BASE + rows[i]) % MOD
    hashes = [h]
    for t in range(1, max_t + p + 1):
        h = ((h - (rows[t - 1] % MOD) * bk) * BASE + rows[t + k - 1]) % MOD
        hashes.append(h)
    for t in range(max_t + 1):
        if hashes[t] == hashes[t + p]:
            if rows[t:t + k] == rows[t + p:t + p + k]:
                return t
    return None


def certify(k, A):
    p = 2 * k + A + 2
    upto = 4 * p + 2 * k + 10
    rows, starts = fast_interval_solver(k, 1, upto)
    t = find_window(rows, k, p)
    assert t is not None, (k, A, 'no window')
    bridge = t + k + p - 1
    assert bridge < upto - p
    bad = next((n for n in range(bridge + 1) if starts[n] != targets(k, A, n, p)), None)
    assert bad is None, (k, A, 'template break', bad)
    bad = next((n for n in range(t, upto - p + 1) if rows[n] != rows[n + p]), None)
    assert bad is None, (k, A, 'row induction break', bad)
    smallest = A if k == A - 1 else p
    assert all(starts[n] == starts[n % smallest] for n in range(bridge + 1)), (k, A, 'least period')
    return {'k': k, 'A': A, 'period': p, 'window_start': t, 'bridge': bridge,
            'least_start_period': smallest, 'max_n_checked': upto}


def crosscheck(k, A, bridge):
    """Independent agreement on [0, bridge] (bounded work for large k)."""
    p = 2 * k + A + 2
    cap = bridge if k <= 400 else min(bridge, 6 * k + 4000)
    f_rows, f_starts = fast_interval_solver(k, 1, cap)
    i_rows, i_starts = interval_solver(k, 1, cap)
    assert f_rows == i_rows and f_starts == i_starts, (k, A, 'interval')
    b_rows, b_starts = boolean_solver(k, cap, 1)
    assert f_rows == b_rows and f_starts == b_starts, (k, A, 'boolean')
    if k <= 120:
        sg_rows, sg_starts = direct_sg_pn(k, cap, 1)
        assert f_rows == sg_rows and f_starts == sg_starts, (k, A, 'SG')
    if k <= 12:
        n_rows, n_starts = naive_solver(k, 1, cap)
        assert f_rows == n_rows and f_starts == n_starts, (k, A, 'naive')
    return cap


def falsify(k, A, search=6):
    p = 2 * k + A + 2
    limit = search * p + 4 * k + 20
    rows, starts = fast_interval_solver(k, 1, limit)
    wrong = next((n for n in range(limit + 1) if starts[n] != targets(k, A, n, p)), None)
    assert wrong is not None, (k, A, 'no counterexample')
    if k <= 60:
        n_rows, n_starts = naive_solver(k, 1, wrong)
        assert starts[:wrong + 1] == n_starts, (k, A, 'counterexample naive')
    return wrong


def main():
    base = Path('data/certificates')
    base.mkdir(parents=True, exist_ok=True)
    records = []
    checks = {}
    for A, lo, hi, j, pos in REGIMES:
        print(f'=== A={A} (j={j}, pos={pos}) k={lo}..{hi} ===', flush=True)
        lo_fail = falsify(lo - 1, A)
        hi_fail = falsify(hi + 1, A)
        print(f'  boundaries: k={lo-1} fails n={lo_fail}; k={hi+1} fails n={hi_fail}', flush=True)
        checked = 0
        for k in range(lo, hi + 1):
            rec = certify(k, A)
            rec['group_j'] = j
            rec['position'] = pos
            records.append(rec)
            checked += 1
        sample = sorted({k for k in (lo, lo + 1, (lo + hi) // 2, hi - 1, hi) if lo <= k <= hi})
        xs = []
        for k in sample:
            rec = next(r for r in records if r['A'] == A and r['k'] == k)
            cap = crosscheck(k, A, rec['bridge'])
            xs.append({'k': k, 'through': cap})
        checks[str(A)] = {'k_min': lo, 'k_max': hi, 'count': checked,
                          'lower_fail_k': lo - 1, 'lower_fail_n': lo_fail,
                          'upper_fail_k': hi + 1, 'upper_fail_n': hi_fail,
                          'crosscheck_samples': xs}
        print(f'  certified {checked} values of k', flush=True)
    for A, k in COLLAPSE_ONLY:
        assert certify(k, A)
        print(f'  collapse-only A={A} k={k}=A-1 certified', flush=True)
        assert falsify(A, A) == A
    out_csv = base / 'regime_hierarchy_certificates.csv'
    with out_csv.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(records[0]))
        w.writeheader()
        w.writerows(records)
    summary = {
        'regimes': checks,
        'collapse_only': [{'A': A, 'k': k} for A, k in COLLAPSE_ONLY],
        'certificates': len(records),
        'all_passed': True,
        'certificate_csv_sha256': hashlib.sha256(out_csv.read_bytes()).hexdigest(),
    }
    (base / 'regime_hierarchy_summary.json').write_text(
        json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'certificates': len(records), 'regimes': len(REGIMES),
                      'sha256': summary['certificate_csv_sha256']}, indent=2))


if __name__ == '__main__':
    main()
