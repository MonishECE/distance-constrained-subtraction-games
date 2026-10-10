#!/usr/bin/env python3
"""Dry-run by default. Replace tracked files on a clean, pinned NEW local branch."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--apply',action='store_true')
    args=parser.parse_args()
    package=Path(__file__).resolve().parents[1]
    repo=args.repo.resolve()
    def git(*argv):return subprocess.check_output(['git','-C',str(repo),*argv],stderr=subprocess.STDOUT).decode().strip()
    if Path(git('rev-parse','--show-toplevel')).resolve()!=repo:raise SystemExit('Choose the repository root.')
    if repo==package or repo in package.parents or package in repo.parents:raise SystemExit('Package and checkout must be separate, non-nested folders.')
    url=git('remote','get-url','origin').removesuffix('.git').lower()
    if url not in ['https://github.com/monishece/distance-constrained-subtraction-games','git@github.com:monishece/distance-constrained-subtraction-games']:
        raise SystemExit('Origin is not the intended GitHub repository.')
    branch=git('branch','--show-current')
    if not branch or branch in ['main','master','research/formal-theorems-a-b-c']:
        raise SystemExit('Create and switch to a NEW local branch first.')
    snapshot=json.loads((package/'migration/BRANCH_SNAPSHOT.json').read_text())
    head=git('rev-parse','HEAD')
    if head not in snapshot.values():raise SystemExit('HEAD differs from the audited branch snapshot. Refresh the audit before replacing.')
    if git('status','--porcelain','--untracked-files=all') or git('ls-files','--others'):
        raise SystemExit('Checkout must be clean with no untracked or ignored files. Use a fresh clone.')
    files=[]
    for line in (package/'MANIFEST_SHA256.txt').read_text().splitlines():
        digest,name=line.split('  ',1);source=package/name
        target=(repo/name).resolve()
        if repo not in target.parents or '.git' in target.relative_to(repo).parts:raise SystemExit('Unsafe manifest path.')
        if source.is_symlink() or hashlib.sha256(source.read_bytes()).hexdigest()!=digest:raise SystemExit('Package integrity failure: '+name)
        files.append((source,target))
    files.append((package/'MANIFEST_SHA256.txt',repo/'MANIFEST_SHA256.txt'))
    tracked=git('ls-files','-z').split('\0')
    paths=[]
    for name in filter(None,tracked):
        target=(repo/name).resolve()
        if repo not in target.parents or '.git' in target.relative_to(repo).parts:raise SystemExit('Unsafe tracked path.')
        if (repo/name).is_symlink():raise SystemExit('Symlink checkout unsupported.')
        paths.append(target)
    print('Branch:',branch,'pinned HEAD:',head)
    print('Remove/replace',len(paths),'tracked old files; copy',len(files),'package files.')
    print('Review migration/DELETION_AUDIT.csv before --apply. No remote operation is performed.')
    if not args.apply:return
    backup=repo.parent/(repo.name+'-before-consolidation-'+head[:12]+'.bundle')
    if backup.exists():raise SystemExit('Backup already exists; choose a fresh clone or relocate the existing backup.')
    git('bundle','create',str(backup),'--all')
    # Delete individually checked tracked files only; never recursively delete directories or .git.
    for target in paths:target.unlink()
    for source,target in files:
        target.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(source,target)
    print('Applied locally. Backup:',backup)
    print('Run package verification, then git add -A and inspect the staged diff. Nothing was committed or pushed.')


if __name__=='__main__':main()
