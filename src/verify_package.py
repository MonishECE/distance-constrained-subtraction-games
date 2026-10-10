#!/usr/bin/env python3
"""Verify research evidence in a temporary copy without changing published files."""
import csv
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile


def main():
    assert __debug__, 'Run without -O'
    root=Path(__file__).resolve().parents[1]
    for p in (root/'overleaf').glob('*.tex'):
        assert not re.search(r'\\(?:input|include|includegraphics|bibliography)\{',p.read_text()), p
    with tempfile.TemporaryDirectory() as td:
        temp=Path(td)
        shutil.copytree(root/'src',temp/'src',ignore=shutil.ignore_patterns('__pycache__'))
        for command in [
            ['src/distance_subtraction_research.py','self-test'],
            ['src/affine_region_extractor.py','self-test'],
            ['src/verify_theorems_ab.py'], ['src/verify_theorem_c.py'],
            ['src/full_state_analysis.py','certificates','--out','data/certificates/full_state_period_certificates_k58_78.csv']]:
            result=subprocess.run([sys.executable,*command],cwd=temp,capture_output=True,text=True)
            assert result.returncode==0, (command,result.stdout,result.stderr)
            print('PASS', ' '.join(command))
        for p in (temp/'data/certificates').iterdir():
            assert p.read_bytes()==(root/'data/certificates'/p.name).read_bytes(), ('nonreproducible certificate',p.name)
        for name,body in [('B','theorem_B'),('C','theorem_C')]:
            file=temp/'data/certificates'/('theorem_B_audit.csv' if name=='B' else 'theorem_C_certificates.csv')
            rows=list(csv.DictReader(file.open()))
            tex=(root/'paper'/body/'body.tex').read_text()
            for row in rows:
                k=int(row['k']); p=int(row.get('period',row.get('candidate_period')))
                numbers=[k,p]
                if name=='C':numbers.append(int(row['least_start_period']))
                numbers += [int(row['window_start']),int(row['bridge_through_inclusive'])]
                pattern=r'\s*&\s*'.join(map(str,numbers))+r'\s*&\s*PASS'
                assert re.search(pattern,tex), ('paper table mismatch',name,k,numbers)
                if name=='C':
                    residues={0,54,k+55}
                    bits=[n in residues for n in range(p)]
                    least=next(d for d in range(1,p+1)
                               if all(bits[n]==bits[(n+d)%p] for n in range(p)))
                    assert least==int(row['least_start_period']), ('C minimality',k)
        failures=list(csv.DictReader((temp/'data/certificates/theorem_C_boundary_counterexamples.csv').open()))
        tex=(root/'paper/theorem_C/body.tex').read_text()
        for row in failures:
            numbers=[row['k'],row['A'],row['first_counterexample_n']]
            assert re.search(r'\s*&\s*'.join(numbers),tex), ('boundary table',row)
    print('PASS: solver self-tests, standalone structure, reproduced certificates and paper tables')


if __name__=='__main__': main()
