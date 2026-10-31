#!/usr/bin/env python3
"""Generate standalone Overleaf main/C sources from canonical modular sources."""
import argparse
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INPUT = re.compile(r'\\input\{([^}]+)\}')


def expand(path):
    text = path.read_text(encoding='utf-8')
    return INPUT.sub(lambda m: expand((path.parent / m[1]).resolve()), text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for source, dest in [('paper/main.tex', 'overleaf/main.tex'),
                         ('paper/theorem_C/main.tex', 'overleaf/theorem_C.tex')]:
        expected = expand(ROOT / source)
        path = ROOT / dest
        if args.check:
            assert path.read_text(encoding='utf-8') == expected, dest
        else:
            path.write_text(expected, encoding='utf-8')
        print('PASS' if args.check else 'SYNC', dest)


if __name__ == '__main__':
    main()
