#!/usr/bin/env python3
"""Verify integrity and research in a temporary copy without changing the package."""
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
    manifest=root/'MANIFEST_SHA256.txt'
    expected={}
    for line in manifest.read_text().splitlines():
        digest,path=line.split('  ',1); expected[path]=digest
        assert hashlib.sha256((root/path).read_bytes()).hexdigest()==digest, ('hash mismatch',path)
    actual={p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file()
            and '__pycache__' not in p.parts and '.git' not in p.relative_to(root).parts
            and p.relative_to(root).as_posix()!='MANIFEST_SHA256.txt'}
    assert actual==set(expected), ('unlisted/missing files',actual.symmetric_difference(expected))
    audit=list(csv.DictReader((root/'migration/DELETION_AUDIT.csv').open(encoding='utf-8')))
    for row in audit:
        assert hashlib.sha256((root/row['preserved_at']).read_bytes()).hexdigest()==row['sha256'], row
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
    print(f'PASS: manifest ({len(expected)} files), all {len(audit)} source mappings, standalone structure, reproduced evidence and paper tables')


if __name__=='__main__': main()
