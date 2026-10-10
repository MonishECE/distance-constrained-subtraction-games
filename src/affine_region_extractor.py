#!/usr/bin/env python3
"""Exact full-state P-region mining for D(k,1).

Produces reproducible, *exploratory* affine segments, cross-parameter tracks,
full-state truth tables, and exhaustive cycle/formula checks. Segments are
geometric descriptions of computed points, not symbolic game-theory proofs.

Run: python src/affine_region_extractor.py batch --k-min 58 --k-max 78 --out results/affine
"""
from __future__ import annotations
import argparse
import csv
import re
from collections import defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
from typing import NamedTuple

from full_state_analysis import boolean_solver, direct_sg_pn, earliest_cycle_start

# Coordinates are (s,n), with n a residue in [0,p). We do not merge at the
# modular seam; those pieces can later be given an explicitly modular formula.
DIRECTIONS = ((0,1),(1,0),(1,1),(1,-1),(1,2),(1,-2),(2,1),(2,-1),(1,3),(1,-3),(3,1),(3,-1))

class Segment(NamedTuple):
    k: int
    period: int
    ds: int
    dn: int
    c: int                 # invariant ds*n - dn*s
    s0: int
    n0: int
    s1: int
    n1: int
    length: int
    component_id: int
    selected: bool
    def cells(self):
        return tuple((self.s0+j*self.ds, self.n0+j*self.dn) for j in range(self.length))
    def slope_label(self):
        if self.ds == 0: return 'vertical: s=constant'
        return str(Fraction(self.dn,self.ds))
    def formula(self):
        if self.ds == 0: return f's={self.s0}; {min(self.n0,self.n1)}<=n<={max(self.n0,self.n1)}'
        if self.dn == 0: return f'n={self.n0}; {self.s0}<=s<={self.s1}'
        return f'{self.ds}*n-{self.dn}*s={self.c}; {self.s0}<=s<={self.s1}; (s,n)=({self.s0},{self.n0})+j*({self.ds},{self.dn})'


def make_cells(rows: list[int], k:int, period:int) -> set[tuple[int,int]]:
    return {(s,n) for n in range(period) for s in range(1,k+1)
            if rows[n] & (1 << (s-1))}


def components(cells: set[tuple[int,int]]):
    """8-neighbor components within one unwrapped period; no seam connection."""
    labels = {}
    counts = []
    cid = 0
    for seed in sorted(cells):
        if seed in labels: continue
        todo = deque([seed]); labels[seed] = cid; count=0
        while todo:
            s,n = todo.popleft(); count+=1
            for ds in (-1,0,1):
                for dn in (-1,0,1):
                    if ds==dn==0: continue
                    nxt=(s+ds,n+dn)
                    if nxt in cells and nxt not in labels:
                        labels[nxt]=cid; todo.append(nxt)
        counts.append(count); cid+=1
    return labels,counts


def maximal_segments(k,period,cells,labels,min_length=3):
    """Every maximal consecutive chain along a reduced primitive direction."""
    segs=[]
    for ds,dn in DIRECTIONS:
        for s,n in sorted(cells):
            if (s-ds,n-dn) in cells: continue
            length=1
            while (s+length*ds,n+length*dn) in cells:
                length+=1
            if length < min_length: continue
            end_s=s+(length-1)*ds
            end_n=n+(length-1)*dn
            segs.append(Segment(k,period,ds,dn,ds*n-dn*s,s,n,end_s,end_n,
                                length,labels[(s,n)],False))
    return segs


def select_cover(cells,segments):
    """Deterministic exact greedy line cover; leftover points remain explicit."""
    pending=set(cells)
    candidates=[(seg,set(seg.cells())) for seg in segments]
    chosen=[]
    while True:
        score,ind=max(((len(covered & pending),i) for i,(_,covered) in enumerate(candidates)),
                      default=(0,-1))
        if score < 3: break
        seg,covered=candidates[ind]
        chosen.append(seg._replace(selected=True))
        pending.difference_update(covered)
    return chosen,pending


def verify_periodic(k,rows,starting,p,t):
    """Check finite-window P/N certificate and start formula. Returns independent facts."""
    window_ok = t is not None and rows[t:t+k] == rows[t+p:t+p+k]
    residues={0,86,k+87}
    checked = t + k + p - 1 if t is not None else -1
    start_ok = t is not None and all(starting[n]==(n%p in residues) for n in range(checked+1))
    return bool(window_ok),bool(start_ok),checked


def analyze(k:int,min_length:int=3,check_sg:bool=False):
    if not 58<=k<=78:
        raise ValueError('Affine template is currently certified only for k in 58..78')
    p=2*k+88
    nmax=3*p+2*k+10
    rows,starting=boolean_solver(k,nmax,1)
    t=earliest_cycle_start(rows,k,p)
    cert_ok,start_ok,prefix=verify_periodic(k,rows,starting,p,t)
    if not (cert_ok and start_ok):
        raise AssertionError(f'Period or residue verification failed at k={k}')
    sg_ok=None
    if check_sg:
        stop=t+p+k-1
        sg_rows,sg_start=direct_sg_pn(k,stop,1)
        sg_ok=(rows[:stop+1]==sg_rows and starting[:stop+1]==sg_start)
        if not sg_ok: raise AssertionError(f'SG cross-check failed for k={k}')
    cells=make_cells(rows,k,p)
    labels,component_sizes=components(cells)
    candidates=maximal_segments(k,p,cells,labels,min_length)
    selected,uncovered=select_cover(cells,candidates)
    # Exhaustive exact reconstruction: no false positives, no false negatives.
    reconstructed=set(uncovered)
    for seg in selected: reconstructed.update(seg.cells())
    fp=reconstructed-cells; fn=cells-reconstructed
    if fp or fn: raise AssertionError('Cover reconstruction failed')
    # Check whether the FIRST-period diagram itself repeats from n=0.
    whole_period_equal=all(rows[n]==rows[n+p] for n in range(p))
    return dict(k=k,period=p,cycle_start=t,certificate=cert_ok,starting_formula=start_ok,
                prefix_checked_through=prefix,sg_crosscheck=sg_ok,
                starting_residues=','.join(map(str,sorted({n for n in range(p) if starting[n]}))),
                full_state_repeats_from_zero=whole_period_equal,
                p_cells=len(cells),n_components=len(component_sizes),
                candidate_segments=len(candidates),selected_segments=len(selected),
                uncovered_cells=len(uncovered),false_positives=len(fp),false_negatives=len(fn),
                coverage_fraction=round(1-len(uncovered)/len(cells),6) if cells else 1.0,
                cells=cells,labels=labels,components=component_sizes,
                candidates=candidates,selected=selected,uncovered=uncovered,rows=rows)


def save_csv(path,rows,fieldnames=None):
    path=Path(path); path.parent.mkdir(parents=True,exist_ok=True)
    if fieldnames is None: fieldnames=list(rows[0]) if rows else []
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fieldnames,extrasaction='ignore'); w.writeheader();w.writerows(rows)


def seg_record(seg):
    return dict(k=seg.k,p=seg.period,ds=seg.ds,dn=seg.dn,slope=seg.slope_label(),
                invariant_c=seg.c,s_min=seg.s0,n_at_s_min=seg.n0,
                s_max=seg.s1,n_at_s_max=seg.n1,length=seg.length,
                component_id=seg.component_id,selected=seg.selected,formula=seg.formula())


def affine_formula(values):
    """Exact integer affine fit y=a*k+b for any >=2 distinct ks, or None."""
    if len(values)<2:return None
    (k1,v1),(k2,v2)=values[:2]
    slope=Fraction(v2-v1,k2-k1)
    offset=Fraction(v1)-slope*k1
    if any(slope*k+offset!=v for k,v in values):return None
    return slope,offset


def fmt_affine(formula):
    if formula is None:return 'not affine'
    a,b=formula
    return f'({a})*k+({b})'


def find_tracks(all_results,min_support=4):
    """Exact affine candidate tracks, requiring absence of ambiguity at each k.

    Seed two different ks and extrapolate segment invariant c, endpoints and
    length; match remaining ks by all exact fields. This is deliberately strict,
    and does not claim an unproved global formula.
    """
    keys=sorted(all_results)
    byk={k:all_results[k]['selected'] for k in keys}
    # Pairwise seed across consecutive k. If identical segment orientations
    # have numerous options, require matching all affine fields.
    seen=set(); tracks=[]
    for k1,k2 in zip(keys,keys[1:]):
        for a in byk[k1]:
            for b in byk[k2]:
                if (a.ds,a.dn)!=(b.ds,b.dn):continue
                attrs=['c','s0','n0','s1','n1','length']
                fs={field:affine_formula([(k1,getattr(a,field)),(k2,getattr(b,field))]) for field in attrs}
                members=[]
                for k in keys:
                    match=[seg for seg in byk[k] if (seg.ds,seg.dn)==(a.ds,a.dn)
                          and all(Fraction(getattr(seg,field))==fs[field][0]*k+fs[field][1] for field in attrs)]
                    if len(match)==1:members.append((k,match[0]))
                if len(members)<min_support:continue
                # Must be a consecutive parameter interval.
                by_key={k:s for k,s in members}; runs=[];run=[]
                for k in keys:
                    if k in by_key:run.append((k,by_key[k]))
                    else:
                        if len(run)>=min_support:runs.append(run)
                        run=[]
                if len(run)>=min_support:runs.append(run)
                for run in runs:
                    sig=(a.ds,a.dn,tuple((f,str(fs[f][0]),str(fs[f][1])) for f in attrs),run[0][0],run[-1][0])
                    if sig in seen:continue
                    seen.add(sig)
                    tracks.append(dict(direction=f'({a.ds},{a.dn})',slope=a.slope_label(),
                                       k_min=run[0][0],k_max=run[-1][0],support=len(run),
                                       **{f+'_of_k':fmt_affine(fs[f]) for f in attrs}))
    tracks.sort(key=lambda r:(-r['support'],r['direction'],r['k_min']))
    return tracks


def eval_affine(expr,k):
    match=re.fullmatch(r"\(([-0-9/]+)\)\*k\+\(([-0-9/]+)\)",expr)
    if not match: raise ValueError(f"Bad affine formula: {expr}")
    value=Fraction(match.group(1))*k+Fraction(match.group(2))
    if value.denominator!=1: raise ValueError(f"Nonintegral endpoint at k={k}: {expr}")
    return int(value)


def validate_track_union(results,tracks):
    """Track-only *candidate* vs exhaustive full-state truth table; report misses."""
    output=[]
    for k,r in sorted(results.items()):
        predicted=set()
        active=0
        for tr in tracks:
            if not tr['k_min']<=k<=tr['k_max']:continue
            active+=1
            ds,dn=map(int,tr['direction'].strip('()').split(','))
            vals={f:eval_affine(tr[f+'_of_k'],k) for f in ('s0','n0','s1','n1','length','c')}
            for j in range(vals['length']):
                s=vals['s0']+ds*j;n=vals['n0']+dn*j
                if not (1<=s<=k and 0<=n<r['period']):
                    raise AssertionError(f'Track out of bounds at k={k}')
                if ds*n-dn*s!=vals['c']:
                    raise AssertionError('Track invariant mismatch')
                predicted.add((s,n))
        fp=predicted-r['cells']; fn=r['cells']-predicted
        output.append(dict(k=k,active_tracks=active,tracked_cells=len(predicted),
                           actual_p_cells=len(r['cells']),false_positives=len(fp),
                           false_negatives=len(fn),recall=round(1-len(fn)/len(r['cells']),6),
                           exact_complete=(not fp and not fn)))
    return output


def test_boundary_formula(ks=(56,57,79,80),repeats=3):
    """Attempt falsification outside fitted interval, no assertion of periodicity."""
    output=[]
    for k in ks:
        p=2*k+88
        _,starting=boolean_solver(k,repeats*p,1)
        expected={0,86,k+87}
        mismatch=[n for n in range(repeats*p+1)
                  if starting[n] != (n%p in expected)]
        output.append(dict(k=k,period_tested=p,through_n=repeats*p,
                           mismatches=len(mismatch),first_mismatch=mismatch[0] if mismatch else '',
                           matched_finite_prefix=(not mismatch)))
    return output


def write_results(results,out,min_support=4):
    out=Path(out);out.mkdir(parents=True,exist_ok=True)
    public=['k','period','cycle_start','certificate','starting_formula',
            'prefix_checked_through','sg_crosscheck','starting_residues',
            'full_state_repeats_from_zero','p_cells','n_components',
            'candidate_segments','selected_segments','uncovered_cells',
            'coverage_fraction','false_positives','false_negatives']
    save_csv(out/'summary.csv', [r for _,r in sorted(results.items())],public)
    save_csv(out/'selected_regions.csv',
             [seg_record(seg) for _,res in sorted(results.items()) for seg in res['selected']])
    save_csv(out/'maximal_segments.csv',
             [seg_record(seg) for _,res in sorted(results.items()) for seg in res['candidates']])
    save_csv(out/'residual_points.csv',
             [dict(k=k,p=res['period'],s=s,n=n) for k,res in sorted(results.items())
              for s,n in sorted(res['uncovered'])],['k','p','s','n'])
    save_csv(out/'component_sizes.csv',
             [dict(k=k,component_id=i,size=size) for k,r in sorted(results.items())
              for i,size in enumerate(r['components'])],['k','component_id','size'])
    tracks=find_tracks(results,min_support)
    save_csv(out/'exact_affine_tracks.csv',tracks,
             ['direction','slope','k_min','k_max','support']+
             [f+'_of_k' for f in ['c','s0','n0','s1','n1','length']])
    track_validation=validate_track_union(results,tracks)
    save_csv(out/'track_only_validation.csv',track_validation)
    boundary=test_boundary_formula()
    save_csv(out/'boundary_falsification.csv',boundary)
    write_summary(out,results,tracks,track_validation,boundary)
    return tracks


def write_summary(out,results,tracks,track_validation,boundary):
    ks=sorted(results)
    summary=(f'# Exact affine-region exploration: k={ks[0]}..{ks[-1]}\n\n'
      'All equations here are **exact descriptions of computed P-state points** '
      'inside the *first* starting period `0 <= n < p(k)`. '
      'They are not yet symbolic theorems for every k or a complete human proof.\n\n'
      '## Methods\n\n'
      '- Generate Boolean P-state coordinates from an independent exact recurrence.\n'
      '- Verify k-row cycle equality and starting residues via a finite-state certificate.\n'
      '- Independently check SG P/N output when `--crosscheck-sg` is selected.\n'
      '- Extract all maximal consecutive segments with primitive integer directions '
      'and exact invariant `ds*n - dn*s = c`.\n'
      '- Build a greedy exact line cover; store uncovered points explicitly.\n'
      '- Reconstruct each first-period P set from selected lines + residual points '
      'and count false positives/negatives exhaustively.\n'
      '- Match segments across k using exact rational affine formulas for '
      'invariant, endpoints, and length; report only contiguous exact matches.\n\n'
      '## Summary\n\n'
      '| k | p | P cells | lines | residual | covered % | full-state period from 0 |\n'
      '|---:|---:|---:|---:|---:|---:|:---:|\n')
    for k in ks:
        r=results[k]
        summary+=(f"| {k} | {r['period']} | {r['p_cells']} | {r['selected_segments']} | "
                  f"{r['uncovered_cells']} | {100*r['coverage_fraction']:.1f} | "
                  f"{'yes' if r['full_state_repeats_from_zero'] else 'no'} |\n")
    summary+=f'\n## Exact cross-parameter tracks\n\n{len(tracks)} qualifying contiguous tracks.\n\n'
    for tr in tracks[:25]:
        summary+=(f"- **k={tr['k_min']}..{tr['k_max']}**, direction {tr['direction']}, "
                  f"invariant `c={tr['c_of_k']}`, `s0={tr['s0_of_k']}`, "
                  f"`n0={tr['n0_of_k']}`, `s1={tr['s1_of_k']}`, `n1={tr['n1_of_k']}`\n")
    summary+='\n## Track-only classification validation\n\n'
    summary+='| k | active tracks | true P-cells | covered by tracks | false positives | false negatives |\n'
    summary+='|---:|---:|---:|---:|---:|---:|\n'
    for row in track_validation:
        summary+=(f"| {row['k']} | {row['active_tracks']} | {row['actual_p_cells']} | "
                  f"{row['tracked_cells']} | {row['false_positives']} | {row['false_negatives']} |\n")
    summary+='\n**Meaning:** Tracked affine families alone are not yet a full symbolic classification unless **both** mismatch counts are zero. The per-k exact cover including residual points is checked separately.\n'
    summary+='\n## Boundary falsification\n\n'
    summary+='| k outside | candidate p | checked through | mismatch count | first mismatch |\n'
    summary+='|---:|---:|---:|---:|---:|\n'
    for row in boundary:
        summary+=(f"| {row['k']} | {row['period_tested']} | {row['through_n']} | "
                  f"{row['mismatches']} | {row['first_mismatch']} |\n")
    summary+='\n## Crucial limitations\n\n'
    summary+=('A region catalog fit on each k does not prove parameter-wide correctness. '
             'The greedy cover is not unique, and connected components can include '
             'overlapping lines or nonlinear boundaries. The region catalog plus '
             'residual points is an **exact finite description** of each analyzed '
             'first period, not automatically a compact uniform symbolic family. '
             'Full-state periodicity for k=58..64 starts only after a transient: '
             'the first period of full state need not reproduce exactly. '
             'No claim is made about k outside the certified 58..78 range.\n')
    (out/'ANALYSIS.md').write_text(summary,encoding='utf-8')


def selftest():
    # Tests don't depend on an assumed affine family.
    for k in range(2,9):
        for m in (0,1,2):
            a,starts=boolean_solver(k,55,m)
            b,sg_starts=direct_sg_pn(k,55,m)
            assert a==b and starts==sg_starts,(k,m)
    for vals,target in [([(58,10),(59,12),(61,16)],(Fraction(2),Fraction(-106))),
                        ([(58,10),(59,12),(61,17)],None)]:
        assert affine_formula(vals)==target
    r=analyze(68,check_sg=True)
    assert r['period']==224 and r['cycle_start']==0 and r['certificate']
    assert r['false_positives']==r['false_negatives']==0
    print('Self-test passed: Boolean vs SG, exact affine fits, and k=68 coverage/certificate')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='cmd',required=True)
    for cmd in ('single','batch'):
        q=sub.add_parser(cmd)
        if cmd=='single':q.add_argument('--k',type=int,default=68)
        else:
            q.add_argument('--k-min',type=int,default=58)
            q.add_argument('--k-max',type=int,default=78)
            q.add_argument('--min-support',type=int,default=4)
        q.add_argument('--min-length',type=int,default=3)
        q.add_argument('--crosscheck-sg',action='store_true')
        q.add_argument('--out',type=Path,default=Path('results/affine'))
    sub.add_parser('self-test')
    args=parser.parse_args()
    if args.cmd=='self-test':return selftest()
    ks=range(args.k_min,args.k_max+1) if args.cmd=='batch' else [args.k]
    results={}
    for k in ks:
        r=analyze(k,args.min_length,args.crosscheck_sg)
        results[k]=r
        print(f"k={k:2d}: p={r['period']}, P-cells={r['p_cells']}, "
              f"lines={r['selected_segments']}, residual={r['uncovered_cells']}, "
              f"coverage={r['coverage_fraction']:.1%}, exact-certificate={r['certificate']}",flush=True)
    tracks=write_results(results,args.out,getattr(args,'min_support',4))
    print(f'Wrote {args.out}; {len(tracks)} exact cross-parameter affine tracks')

if __name__=='__main__':main()
