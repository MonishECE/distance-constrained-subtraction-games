import csv,json,pathlib,sys,subprocess,tempfile,hashlib
root=pathlib.Path(__file__).parent/'audit-repo'
sys.path.insert(0,str(root/'src'))
from verify_theorems_ab import interval_solver

def independent(k,m,N):
 with tempfile.NamedTemporaryFile() as f:
  subprocess.run(['/tmp/independent-pn',str(k),str(m),str(N),f.name],check=True)
  b=pathlib.Path(f.name).read_bytes()
 return [sum(b[n*(k+1)+s]<<(s-1) for s in range(1,k+1)) for n in range(N+1)],[bool(b[n*(k+1)]) for n in range(N+1)]

results={'certificates':[],'boundaries':[],'scans':[],'affine_files':[]}
for k in range(1,21):
 for m in range(0,2*k+2):
  if independent(k,m,150)!=interval_solver(k,m,150):raise RuntimeError(('A crosscheck',k,m))
results['A_extra_parameter_pairs']=sum(2*k+2 for k in range(1,21))
for family,filename,A in [('B','theorem_B_audit.csv',86),('C','theorem_C_certificates.csv',54),('D','theorem_D_certificates.csv',214)]:
 for rec in csv.DictReader((root/'data/certificates'/filename).open()):
  k=int(rec['k']);p=int(rec.get('period',rec.get('candidate_period')));t=int(rec['window_start']);bridge=int(rec['bridge_through_inclusive']);N=12*p+2*k
  rows,starts=independent(k,1,N)
  if (rows,starts)!=interval_solver(k,1,N):raise RuntimeError(('direct disagreement',family,k))
  if rows[t:t+k]!=rows[t+p:t+p+k]:raise RuntimeError(('window',family,k))
  if bridge!=t+k+p-1:raise RuntimeError(('bridge bound',family,k))
  fp=sum(starts[n] and n%p not in {0,A,k+A+1} for n in range(N+1))
  fn=sum(not starts[n] and n%p in {0,A,k+A+1} for n in range(N+1))
  if fp or fn:raise RuntimeError(('template',family,k,fp,fn))
  if not all(rows[n]==rows[n+p] for n in range(t,N-p+1)):raise RuntimeError(('row repeat',family,k))
  results['certificates'].append(dict(family=family,k=k,N=N,false_positives=fp,false_negatives=fn))
 print('independent certificates PASS',family,flush=True)
for family in ['C','D']:
 for rec in csv.DictReader((root/'data/certificates'/f'theorem_{family}_boundary_counterexamples.csv').open()):
  k=int(rec['k']);A=int(rec['A']);p=int(rec['candidate_period']);n=int(rec['first_counterexample_n'])
  _,starts=independent(k,1,n)
  wrong=next(i for i in range(n+1) if starts[i]!=(i%p in {0,A,k+A+1}))
  if wrong!=n or starts[n]!=(rec['actual_P']=='True'):raise RuntimeError(('boundary',rec))
  results['boundaries'].append(dict(family=family,k=k,A=A,n=n,actual_P=starts[n]))
for path in (root/'data').rglob('*scan_results.csv'):
 for rec in csv.DictReader(path.open()):
  if not rec['period']:continue
  k=int(rec['k']);m=int(rec['m']);p=int(rec['period']);pre=int(rec['preperiod']);N=max(5000,pre+8*p+2*k)
  rows,starts=independent(k,m,N)
  residues={int(x) for x in rec['p_residues'].strip('{}').split(',') if x}
  wrong=next((n for n in range(pre,N+1) if starts[n]!=(n%p in residues)),None)
  t=next((n for n in range(pre,N-p-k+2) if rows[n:n+k]==rows[n+p:n+p+k]),None)
  results['scans'].append(dict(file=str(path.relative_to(root)),k=k,m=m,N=N,first_mismatch=wrong,full_PN_witness=t))
 print('supporting scan rows checked',path.name,flush=True)
for path in (root/'results/affine').glob('*'):
 regenerated=pathlib.Path('/tmp/audit-affine')/path.name
 if regenerated.exists():
  same=path.read_text()==regenerated.read_text()
  results['affine_files'].append(dict(file=path.name,text_equal=same))
pathlib.Path('audit-results.json').write_text(json.dumps(results,indent=2))
print(json.dumps({key:len(value) if isinstance(value,list) else value for key,value in results.items()},indent=2))
print('scan mismatches',sum(r['first_mismatch'] is not None for r in results['scans']))
print('scans without full-state witness',sum(r['full_PN_witness'] is None for r in results['scans']))
