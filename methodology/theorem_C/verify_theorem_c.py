#!/usr/bin/env python3
"""Exact fixed-parameter certificates and boundary counterexamples for Theorem C.

No sympy or external packages; NOT a symbolic parameter-uniform proof.
Run from repository root: python methodology/theorem_C/verify_theorem_c.py
"""
from __future__ import annotations
import csv
import hashlib
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / 'theorem_B'))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'src'))
from verify_theorems_ab import interval_solver, naive_solver
from full_state_analysis import direct_sg_pn

CERTIFIED = range(42, 54)
BOUNDARIES = [(41, 54), (54, 54), (55,54), (56,54), (57,54), (57,86), (79,86), (80,86)]


def targets(k, a, n):
    p = 2*k+a+2
    return (n % p) in {0,a,k+a+1}


def certify(k):
    a=54
    p=2*k+a+2
    # Covers all candidate windows with t in [0, 2p] and complete bridge.
    upto = 4*p + 2*k + 10
    rows, starts = interval_solver(k,1,upto)
    ts = [t for t in range(2*p+1)
          if all(rows[t+i] == rows[t+p+i] for i in range(k))]
    assert ts, (k, 'missing exact k-row witness')
    t=ts[0]
    bridge=t+k+p-1
    assert bridge < upto-p
    assert all(starts[n] == targets(k,a,n) for n in range(bridge+1)), (k,'bridge')
    assert all(rows[n] == rows[n+p] for n in range(t, upto-p+1)), (k,'row induction spot-check')
    sg_rows, sg_starts = direct_sg_pn(k, bridge, m=1)
    assert rows[:bridge+1] == sg_rows, (k,'independent SG rows')
    assert starts[:bridge+1] == sg_starts, (k,'independent SG starts')
    # 53 is the arithmetic degeneracy k=a-1; its start least period is a.
    smallest = (a if k==a-1 else p)
    assert all(starts[n]==starts[n%smallest] for n in range(bridge+1))
    # The 3-point pattern admits a smaller shift iff k=a-1, via the coset lemma.
    return {'k':k,'A':a,'candidate_period':p,'least_start_period':smallest,
            'window_start':t,'window_size':k,'bridge_through_inclusive':bridge,
            'start_residues':f'0,{a},{k+a+1}', 'SG_crosscheck':'PASS','status':'PROVED: fixed-k certificate'}


def falsify(k,a):
    p=2*k+a+2
    limit=4*p+4*k+10
    rows,starts=interval_solver(k,1,limit)
    wrong=next((n for n in range(limit+1) if starts[n] != targets(k,a,n)), None)
    assert wrong is not None, (k,a,'no counterexample found in declared finite search')
    # Independent brute-force small recursion through counterexample
    naive_rows,naive_starts=naive_solver(k,1,wrong)
    assert starts[:wrong+1]==naive_starts, (k,a,'counterexample disagreement')
    assert rows[:wrong+1]==naive_rows, (k,a,'counterexample row disagreement')
    return {'k':k,'A':a,'candidate_period':p,'first_counterexample_n':wrong,
            'predicted_P':targets(k,a,wrong),'actual_P':starts[wrong],
            'naive_crosscheck':'PASS','status':'PROVED: proposed template fails at this k'}


def main():
    base=Path('data/certificates')
    base.mkdir(parents=True,exist_ok=True)
    proven=[certify(k) for k in CERTIFIED]
    boundary=[falsify(k,a) for k,a in BOUNDARIES]
    for name,records in [('theorem_C_certificates.csv',proven),('theorem_C_boundary_counterexamples.csv',boundary)]:
        dest=base/name
        with dest.open('w',newline='',encoding='utf-8') as f:
            w=csv.DictWriter(f,fieldnames=list(records[0]));w.writeheader();w.writerows(records)
    checks = {'theorem_C_fixed_k_certificates':len(proven),'parameters':[42,53],
              'boundary_counterexamples':len(boundary),
              'all_passed':True,
              'uniform_symbolic_regime_theorem':'WORKING ON',
              'infinite_A_hierarchy':'WORKING ON',
              'certificate_csv_sha256':hashlib.sha256((base/'theorem_C_certificates.csv').read_bytes()).hexdigest(),
              'boundary_csv_sha256':hashlib.sha256((base/'theorem_C_boundary_counterexamples.csv').read_bytes()).hexdigest()}
    (base/'theorem_C_summary.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(checks,indent=2))
    for row in proven: print(f"k={row['k']:2} t={row['window_start']:3} p={row['candidate_period']:3} least={row['least_start_period']:3} bridge={row['bridge_through_inclusive']} SG=PASS")
    for row in boundary:print(f"counterexample k={row['k']} A={row['A']} n={row['first_counterexample_n']}: predicted={row['predicted_P']} actual={row['actual_P']}")

if __name__=='__main__': main()
