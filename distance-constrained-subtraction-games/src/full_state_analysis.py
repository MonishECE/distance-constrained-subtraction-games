#!/usr/bin/env python3
"""Full-state P/N analysis and exact finite-state period certificates for D(k,1).

This script is intentionally independent of the optimized C++ scanner.  It uses
Boolean P/N recurrence only, can cross-check against a direct Sprague-Grundy
solver on the same finite range, and can generate the k=58..78 certificate CSV
and a representative full-state plot.
"""

from __future__ import annotations

import argparse
import csv
from pathlib import Path
from typing import List, Tuple


def boolean_solver(k: int, n_max: int, m: int = 1) -> Tuple[List[int], List[bool]]:
    """Return bit-packed P/N rows and unrestricted starting P flags.

    Bit s-1 of rows[n] is 1 iff state (n,s) is P for 1 <= s <= k.
    start_p[n] is True iff the unrestricted starting state with heap n is P.
    """
    if k < 1 or m < 0 or n_max < 0:
        raise ValueError("Require k>=1, m>=0, n_max>=0")

    all_s_mask = (1 << k) - 1
    rows = [0] * (n_max + 1)
    start_p = [False] * (n_max + 1)
    rows[0] = all_s_mask
    start_p[0] = True

    for n in range(1, n_max + 1):
        limit = min(k, n)

        # A_n: removals r that move to a P-state (n-r, r).
        winning_moves = 0
        for r in range(1, limit + 1):
            if rows[n - r] & (1 << (r - 1)):
                winning_moves |= 1 << (r - 1)

        start_p[n] = winning_moves == 0

        row_bits = 0
        for s in range(1, k + 1):
            lo = max(1, s - m)
            hi = min(k, s + m)
            forbidden = ((1 << (hi - lo + 1)) - 1) << (lo - 1)
            # (n,s) is P iff every move to a P-child is forbidden.
            if winning_moves & ~forbidden == 0:
                row_bits |= 1 << (s - 1)
        rows[n] = row_bits

    return rows, start_p


def direct_sg_pn(k: int, n_max: int, m: int = 1) -> Tuple[List[int], List[bool]]:
    """Independent direct SG solver, returned only as P/N rows + start P flags."""
    g = [[0] * (k + 1) for _ in range(n_max + 1)]
    start_p = [False] * (n_max + 1)
    start_p[0] = True

    for n in range(1, n_max + 1):
        limit = min(k, n)
        for s in range(1, k + 1):
            child_values = {
                g[n - r][r]
                for r in range(1, limit + 1)
                if abs(r - s) > m
            }
            mex = 0
            while mex in child_values:
                mex += 1
            g[n][s] = mex

        start_children = {g[n - r][r] for r in range(1, limit + 1)}
        mex = 0
        while mex in start_children:
            mex += 1
        start_p[n] = mex == 0

    rows = []
    for n in range(n_max + 1):
        bits = 0
        for s in range(1, k + 1):
            if g[n][s] == 0:
                bits |= 1 << (s - 1)
        rows.append(bits)
    return rows, start_p


def earliest_cycle_start(rows: List[int], k: int, period: int) -> int | None:
    """Find earliest t with two identical k-row windows separated by period."""
    max_t = len(rows) - period - k
    for t in range(max_t + 1):
        if rows[t : t + k] == rows[t + period : t + period + k]:
            return t
    return None


def verify_start_formula(start_p: List[bool], period: int, residues: set[int], through: int) -> bool:
    through = min(through, len(start_p) - 1)
    return all(start_p[n] == ((n % period) in residues) for n in range(through + 1))


def certify_k(k: int, m: int = 1, sg_crosscheck: bool = True) -> dict:
    if m != 1:
        raise ValueError("Current affine certificate formula is specifically for m=1")

    period = 2 * k + 88
    residues = {0, 86, k + 87}
    n_max = 2 * period + 2 * k + 10
    rows, start_p = boolean_solver(k, n_max, m)
    t = earliest_cycle_start(rows, k, period)
    if t is None:
        raise RuntimeError(f"No {period}-cycle certificate found for k={k} in n<= {n_max}")

    # Once the k-row state window repeats at t and t+p, deterministic finite
    # memory forces all later P/N rows to repeat.  To establish the claimed
    # start-position formula from n=0, it is enough to check the finite prefix
    # up through t+p-1.
    prefix_through = t + k + period - 1
    formula_ok = verify_start_formula(start_p, period, residues, prefix_through)

    sg_ok = True
    if sg_crosscheck:
        check_n = t + period + k - 1
        sg_rows, sg_start = direct_sg_pn(k, check_n, m)
        sg_ok = rows[: check_n + 1] == sg_rows and start_p[: check_n + 1] == sg_start

    return {
        "k": k,
        "m": m,
        "period": period,
        "full_PN_cycle_start": t,
        "start_period_certified_from_n0": bool(formula_ok),
        "finite_prefix_check_through_n": prefix_through,
        "start_P_residues": "{" + ",".join(map(str, sorted(residues))) + "}",
        "independent_SG_crosscheck": bool(sg_ok),
    }


def write_certificates(path: Path, k_min: int = 58, k_max: int = 78) -> List[dict]:
    rows = [certify_k(k) for k in range(k_min, k_max + 1)]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return rows


def plot_full_state(k: int, output: Path) -> None:
    try:
        import numpy as np
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise SystemExit("Plotting requires numpy and matplotlib (pip install -r requirements.txt)") from exc

    if not (58 <= k <= 78):
        raise ValueError("This plot command currently uses the observed m=1 affine regime k=58..78")
    p = 2 * k + 88
    rows, _ = boolean_solver(k, p + k, 1)
    matrix = np.zeros((k, p), dtype=int)
    for n in range(p):
        for s in range(1, k + 1):
            matrix[s - 1, n] = 1 if rows[n] & (1 << (s - 1)) else 0

    fig, ax = plt.subplots(figsize=(13, 5.8))
    ax.imshow(matrix, origin="lower", aspect="auto", interpolation="nearest")
    ax.set_xlabel(f"Heap residue n mod {p}")
    ax.set_ylabel("Previous move s")
    ax.set_title(f"Full P-state structure for D({k},1): one certified period")
    fig.tight_layout()
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, dpi=200, bbox_inches="tight")
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="cmd", required=True)

    cert = sub.add_parser("certificates", help="Generate exact finite-state certificate CSV")
    cert.add_argument("--k-min", type=int, default=58)
    cert.add_argument("--k-max", type=int, default=78)
    cert.add_argument("--out", type=Path, default=Path("full_state_period_certificates_k58_78.csv"))

    plot = sub.add_parser("plot", help="Plot one full-state P-position period")
    plot.add_argument("--k", type=int, default=68)
    plot.add_argument("--out", type=Path, default=Path("full_state_k68_p_positions.png"))

    args = parser.parse_args()
    if args.cmd == "certificates":
        rows = write_certificates(args.out, args.k_min, args.k_max)
        for row in rows:
            print(row)
        print(f"Wrote {args.out}")
    elif args.cmd == "plot":
        plot_full_state(args.k, args.out)
        print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
