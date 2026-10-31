#!/usr/bin/env python3
"""Certify the j=13 extension of the regime hierarchy.

Two second-position regimes are added:
    A=13654 (first 1-run of group 13), k=10922..13653
    A=21846 (second 1-run of group 13), k=15018..20025
plus the collapse-only A=30038 at k=30037.

Records are appended to a JSONL checkpoint so an interrupted run resumes.
Usage: python src/verify_j13.py [A]
"""
from __future__ import annotations

import csv
import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, 'src')
from verify_hierarchy import certify, falsify

REGIMES = [(13654, 10922, 13653), (21846, 15018, 20025)]
COLLAPSE = (30038, 30037)
BASE = Path('data/certificates')
CHECKPOINT = BASE / 'regime_hierarchy_j13_records.jsonl'


def load_done():
    done = {}
    if CHECKPOINT.exists():
        for line in CHECKPOINT.read_text(encoding='utf-8').splitlines():
            if line.strip():
                rec = json.loads(line)
                done[(rec['A'], rec['k'])] = rec
    return done


def main():
    BASE.mkdir(parents=True, exist_ok=True)
    only = int(sys.argv[1]) if len(sys.argv) > 1 else None
    done = load_done()
    with CHECKPOINT.open('a', encoding='utf-8') as f:
        for A, lo, hi in REGIMES:
            if only is not None and A != only:
                continue
            print(f'=== A={A} k={lo}..{hi} ===', flush=True)
            for k in range(lo, hi + 1):
                if (A, k) in done:
                    continue
                rec = certify(k, A)
                f.write(json.dumps(rec) + '\n')
                f.flush()
                done[(A, k)] = rec
                if (k - lo) % 200 == 0:
                    print(f'  k={k} ({k - lo + 1}/{hi - lo + 1})', flush=True)
    print('checkpoint records:', len(done), flush=True)

    all_done = all((A, k) in done for A, lo, hi in REGIMES for k in range(lo, hi + 1))
    if not all_done:
        print('not all records present yet')
        return

    records = [done[(A, k)] for A, lo, hi in REGIMES for k in range(lo, hi + 1)]
    out_csv = BASE / 'regime_hierarchy_j13.csv'
    with out_csv.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(records[0]))
        w.writeheader()
        w.writerows(records)
    boundaries = []
    for A, lo, hi in REGIMES:
        boundaries.append({'A': A, 'k': lo - 1, 'n': falsify(lo - 1, A),
                           'side': 'lower'})
        boundaries.append({'A': A, 'k': hi + 1, 'n': falsify(hi + 1, A),
                           'side': 'upper'})
    A, k = COLLAPSE
    assert certify(k, A)
    boundaries.append({'A': A, 'k': A, 'n': falsify(A, A), 'side': 'collapse'})
    summary = {'regimes': [{'A': A, 'k_min': lo, 'k_max': hi, 'count': hi - lo + 1}
                           for A, lo, hi in REGIMES],
               'collapse_only': [{'A': A, 'k': k}],
               'boundaries': boundaries,
               'certificates': len(records),
               'all_passed': True,
               'certificate_csv_sha256': hashlib.sha256(out_csv.read_bytes()).hexdigest()}
    (BASE / 'regime_hierarchy_j13_summary.json').write_text(
        json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'certificates': len(records),
                      'sha256': summary['certificate_csv_sha256']}, indent=2))


if __name__ == '__main__':
    main()
