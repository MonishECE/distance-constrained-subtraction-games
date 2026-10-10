#!/usr/bin/env python3
"""Reconstructed 2026-10-10 from Theorem A/B text; not the missing original.

Rows are integer bitsets; bit s-1 means (n,s) is P. Exact integer arithmetic.
"""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from full_state_analysis import direct_sg_pn


def interval_solver(k, m, upto):
    if k < 1 or m < 0 or upto < 0:
        raise ValueError('Require k>=1, m>=0, upto>=0')
    full = (1 << k) - 1
    rows, starts = [full], [True]
    for n in range(1, upto + 1):
        moves = [r for r in range(1, min(k, n)+1)
                 if rows[n-r] & (1 << (r-1))]
        starts.append(not moves)
        if not moves:
            rows.append(full)
        else:
            lo, hi = max(1, max(moves)-m), min(k, min(moves)+m)
            rows.append(0 if lo > hi else ((1 << (hi-lo+1))-1) << (lo-1))
    return rows, starts


def naive_solver(k, m, upto):
    if k < 1 or m < 0 or upto < 0:
        raise ValueError('Require k>=1, m>=0, upto>=0')
    # Direct legal-move quantification; no interval construction.
    states = [[True] * (k+1)]
    starts = [True]
    for n in range(1, upto+1):
        states.append([False] + [not any(
            abs(r-s) > m and states[n-r][r]
            for r in range(1, min(k, n)+1)) for s in range(1, k+1)])
        starts.append(not any(states[n-r][r] for r in range(1, min(k,n)+1)))
    return [sum(1 << (s-1) for s in range(1,k+1) if row[s])
            for row in states], starts


def small_checks():
    count = 0
    for k in range(1, 13):
        for m in range(0, 5):
            result = interval_solver(k,m,100)
            assert result == naive_solver(k,m,100), ('naive',k,m)
            assert result == direct_sg_pn(k,100,m), ('SG',k,m)
            count += 1
    return count


def certify(k):
    p = 2*k+88
    upto = 4*p+2*k+10
    rows, starts = interval_solver(k,1,upto)
    t = next((t for t in range(2*p+1)
              if rows[t:t+k] == rows[t+p:t+p+k]), None)
    assert t is not None, ('no witness',k)
    bridge = t+k+p-1
    assert all(starts[n] == (n % p in {0,86,k+87}) for n in range(bridge+1)), ('bridge',k)
    assert (rows[:bridge+1],starts[:bridge+1]) == direct_sg_pn(k,bridge,1), ('SG',k)
    assert rows[:bridge+1] == naive_solver(k,1,bridge)[0], ('naive',k)
    assert all(rows[n] == rows[n+p] for n in range(t,upto-p+1)), ('repeat',k)
    # Exhaust all nonzero cyclic shifts, independent of the analytic minimality lemma.
    pattern = [n in {0,86,k+87} for n in range(p)]
    assert not any(all(pattern[n] == pattern[(n+d)%p] for n in range(p))
                   for d in range(1,p)), ('minimality',k)
    return dict(k=k,m=1,period=p,window_start=t,window_size=k,
                bridge_through_inclusive=bridge,start_residues=f'0,86,{k+87}',
                least_start_period=p,SG_crosscheck='PASS',naive_crosscheck='PASS')


def main():
    assert __debug__, 'Run without Python -O: assertions are part of verification'
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out',type=Path,default=Path('data/certificates/theorem_B_audit.csv'))
    parser.add_argument('--summary',type=Path,default=Path('data/certificates/theorem_B_audit.json'))
    args=parser.parse_args()
    small=small_checks()
    records=[certify(k) for k in range(58,79)]
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
    summary=dict(all_passed=True,small_parameter_crosschecks=small,
                 theorem_B_fixed_k_certificates=len(records),parameters=[58,78],
                 reconstructed_verifier=True,uniform_symbolic_proof=False,
                 certificate_csv_sha256=hashlib.sha256(args.out.read_bytes()).hexdigest())
    args.summary.parent.mkdir(parents=True,exist_ok=True)
    args.summary.write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(summary,indent=2))


if __name__=='__main__':main()
