#!/usr/bin/env python3
"""Audit published j=13 coverage/hash and freshly recertify endpoints.

This is a focused check, not a fresh computation of all 7740 certificates.
"""
import csv
import hashlib
import json
from pathlib import Path
from verify_hierarchy import certify, falsify, find_window


def main():
    root = Path(__file__).resolve().parents[1]
    base = root / 'data/certificates'
    summary = json.loads((base / 'regime_hierarchy_j13_summary.json').read_text())
    path = base / 'regime_hierarchy_j13.csv'
    assert hashlib.sha256(path.read_bytes()).hexdigest() == summary['certificate_csv_sha256']
    with path.open(newline='') as f:
        rows = [{key: int(value) for key, value in row.items()} for row in csv.DictReader(f)]
    expected = {(r['A'], k) for r in summary['regimes']
                for k in range(r['k_min'], r['k_max'] + 1)}
    assert len(rows) == len(expected) == summary['certificates'] == 7740
    assert {(r['A'], r['k']) for r in rows} == expected
    for row in rows:
        k, A, p, t = (row[key] for key in ('k', 'A', 'period', 'window_start'))
        assert p == 2 * k + A + 2
        assert row['bridge'] == t + k + p - 1
        assert row['max_n_checked'] >= row['bridge']
    for regime in summary['regimes']:
        for k in (regime['k_min'], regime['k_max']):
            actual = certify(k, regime['A'])
            assert actual == next(r for r in rows if (r['A'], r['k']) == (regime['A'], k))
    for boundary in summary['boundaries']:
        assert falsify(boundary['k'], boundary['A']) == boundary['n']
    assert certify(30037, 30038)['least_start_period'] == 30038
    # Exercise the late-window and no-window paths, beyond the direct-search shortcut.
    k, p, t = 4, 40, 70
    synthetic = list(range(3 * p + k + 1))
    synthetic[t + p:t + p + k] = synthetic[t:t + k]
    assert find_window(synthetic, k, p) == t
    assert find_window(list(range(3 * p + k + 1)), k, p) is None
    print('PASS: 7740 records, hash/coverage, fresh endpoints, boundaries, collapse, late-window search')


if __name__ == '__main__':
    main()
