#!/usr/bin/env python3
"""
distance_subtraction_research.py

Research engine for distance-constrained dynamic subtraction games.

Game D(k,m)
-----------
There is one heap with n counters. A move removes r counters, where
    1 <= r <= k.
If the previous move removed s counters, the next move must satisfy
    |r - s| > m.
The first move is unrestricted. Normal play: a player with no legal move loses.

What this program does
----------------------
1. Computes P/N positions and Sprague-Grundy (SG) values.
2. Sweeps many k and m values.
3. Detects candidate eventual periods in the starting P-position sequence.
4. Optionally detects a repeated FULL finite state, which certifies a cycle for
   that fixed (k,m) computation.
5. Reports P-position residue classes inside the detected period.
6. Mines simple affine period laws p(k) = a*k + b on congruence classes.
7. Tests a proposed period formula and returns the first counterexample.
8. Writes CSV/Markdown reports for a research notebook.

IMPORTANT NOVELTY WARNING
-------------------------
Computation cannot prove that a mathematical result is new to the literature.
A result is only a novelty candidate until you search the literature and verify
that the theorem/classification has not already been published.

The code is intentionally standard-library only.

Examples
--------
Quick sanity check:
    python distance_subtraction_research.py self-test

Inspect one game:
    python distance_subtraction_research.py single --k 10 --m 1 --n 50000

Scan the proposed ISEF core:
    python distance_subtraction_research.py scan \
        --m-values 1 --k-min 2 --k-max 60 --n 50000 \
        --max-period 10000 --out results_m1

Scan m=0,1,2 for comparison:
    python distance_subtraction_research.py scan \
        --m-values 0 1 2 --k-min 2 --k-max 50 --n 30000 \
        --out comparison_scan

Try to falsify a conjecture p(k)=2k+3 for k == 1 (mod 4):
    python distance_subtraction_research.py test-period-formula \
        --m 1 --k-min 5 --k-max 100 --n 100000 \
        --a 2 --b 3 --q 4 --r 1
"""

from __future__ import annotations

import argparse
import csv
import gc
import hashlib
import math
import sys
from array import array
from dataclasses import dataclass, asdict
from fractions import Fraction
from pathlib import Path
from typing import Iterable, Optional


# ---------------------------------------------------------------------------
# Core utilities
# ---------------------------------------------------------------------------

def mex_from_mask(mask: int) -> int:
    """mex of a set represented by a nonnegative integer bit mask."""
    # The least 0 bit of mask is the least 1 bit of ~mask.
    low_zero = (~mask) & (mask + 1)
    return low_zero.bit_length() - 1


@dataclass
class GameComputation:
    k: int
    m: int
    n_max: int
    table: array        # flat unsigned-short SG table
    start_sg: array     # SG value when no previous move exists
    start_p: bytearray  # 1 exactly when start_sg[n] == 0
    max_state_sg: int


@dataclass
class ScanResult:
    m: int
    k: int
    n_max: int
    preperiod: Optional[int]
    period: Optional[int]
    p_density: Optional[float]
    p_residues: str
    period_fingerprint: str
    max_start_sg: int
    max_state_sg: int
    exact_state_preperiod_upper_bound: Optional[int] = None
    exact_state_period: Optional[int] = None


def solve_game(k: int, m: int, n_max: int) -> GameComputation:
    """
    Compute all SG states g(n, previous_move) for 0 <= n <= n_max.

    Complexity is roughly O(n_max * k * (m+1)) for fixed m, rather than
    O(n_max * k^2), because legal moves are "all moves except a short interval".
    """
    if k < 1:
        raise ValueError("k must be >= 1")
    if m < 0:
        raise ValueError("m must be >= 0")
    if n_max < 0:
        raise ValueError("n_max must be >= 0")
    if k > 65534:
        raise ValueError("k is too large for unsigned-short SG storage.")

    stride = k + 1
    total = (n_max + 1) * stride

    # Grundy values never exceed the number of legal options, hence <= k.
    table = array("H", [0]) * total
    start_sg = array("H", [0]) * (n_max + 1)
    start_p = bytearray(n_max + 1)
    start_p[0] = 1

    children = [0] * (k + 1)
    counts = [0] * (k + 1)
    max_state_sg = 0

    for n in range(1, n_max + 1):
        limit = min(k, n)

        # Build the multiset of SG values reached by every possible subtraction r.
        mask = 0
        used_values = []

        for r in range(1, limit + 1):
            v = table[(n - r) * stride + r]
            children[r] = v
            if counts[v] == 0:
                used_values.append(v)
                mask |= 1 << v
            counts[v] += 1

        # First move: no previous-move restriction.
        sg0 = mex_from_mask(mask)
        start_sg[n] = sg0
        if sg0 == 0:
            start_p[n] = 1

        base = n * stride

        # For each previous move s, temporarily remove forbidden r with |r-s| <= m.
        for s in range(1, k + 1):
            local_mask = mask
            lo = max(1, s - m)
            hi = min(limit, s + m)

            if lo <= hi:
                for r in range(lo, hi + 1):
                    v = children[r]
                    counts[v] -= 1
                    if counts[v] == 0:
                        local_mask &= ~(1 << v)

            g = mex_from_mask(local_mask)
            table[base + s] = g
            if g > max_state_sg:
                max_state_sg = g

            # Restore counts before processing the next s.
            if lo <= hi:
                for r in range(lo, hi + 1):
                    counts[children[r]] += 1

        # Reset only entries touched this n.
        for v in used_values:
            counts[v] = 0

    return GameComputation(
        k=k,
        m=m,
        n_max=n_max,
        table=table,
        start_sg=start_sg,
        start_p=start_p,
        max_state_sg=max_state_sg,
    )


# ---------------------------------------------------------------------------
# Period/cycle detection
# ---------------------------------------------------------------------------

def detect_eventual_period(
    bits: bytearray,
    max_period: int,
    min_repeats: int = 12,
    min_tail: int = 300,
) -> Optional[tuple[int, int]]:
    """
    Find the smallest p <= max_period that is consistent with an eventual
    period over the observed finite sequence.

    Returns (preperiod, period), or None.

    This is a finite-data CONJECTURE detector, not a proof about all n.
    """
    b = bytes(bits)
    L = len(b)

    if L < 3:
        return None

    max_p = min(max_period, max(1, L // max(2, min_repeats)))

    for p in range(1, max_p + 1):
        tail = max(min_tail, p * min_repeats)
        if tail + p > L:
            continue

        start = L - tail - p

        # Fast C-level slice comparison.
        if b[start : L - p] != b[start + p : L]:
            continue

        # Find the last observed disagreement under shift p.
        last_mismatch = -1
        for i in range(0, L - p):
            if b[i] != b[i + p]:
                last_mismatch = i

        pre = last_mismatch + 1

        # Require substantial repeated evidence after the proposed preperiod.
        if L - pre >= p * min_repeats:
            return pre, p

    return None


def detect_exact_full_state_cycle(
    comp: GameComputation,
    max_end: Optional[int] = None,
) -> Optional[tuple[int, int]]:
    """
    Look for an exactly repeated k-row SG state window.

    Once n >= k, the recurrence is translation-invariant. If the entire
    k-row state window repeats, the deterministic recurrence guarantees that
    the future repeats for this fixed (k,m).

    Returns:
        (preperiod_upper_bound, exact_cycle_period)

    This certifies cycling for ONE fixed parameter pair, not a theorem for an
    infinite family of k values.
    """
    k = comp.k
    stride = k + 1
    table = comp.table
    n_max = comp.n_max if max_end is None else min(comp.n_max, max_end)

    # Require the first row of the state window to be at least k.
    first_end = 2 * k - 1
    if n_max < first_end:
        return None

    seen: dict[bytes, list[int]] = {}

    for end in range(first_end, n_max + 1):
        start = end - k + 1
        left = start * stride
        right = (end + 1) * stride
        block = table[left:right].tobytes()
        digest = hashlib.blake2b(block, digest_size=16).digest()

        for old_end in seen.get(digest, []):
            old_start = old_end - k + 1
            old_left = old_start * stride
            old_right = (old_end + 1) * stride

            # Exact byte comparison removes hash-collision ambiguity.
            if table[old_left:old_right].tobytes() == block:
                return old_start, end - old_end

        seen.setdefault(digest, []).append(end)

    return None


def period_description(
    comp: GameComputation,
    max_period: int,
    min_repeats: int,
) -> ScanResult:
    det = detect_eventual_period(
        comp.start_p,
        max_period=max_period,
        min_repeats=min_repeats,
    )

    if det is None:
        return ScanResult(
            m=comp.m,
            k=comp.k,
            n_max=comp.n_max,
            preperiod=None,
            period=None,
            p_density=None,
            p_residues="",
            period_fingerprint="",
            max_start_sg=max(comp.start_sg),
            max_state_sg=comp.max_state_sg,
        )

    pre, p = det
    word = bytes(comp.start_p[pre : pre + p])
    residues = [
        str(n % p)
        for n in range(pre, min(pre + p, comp.n_max + 1))
        if comp.start_p[n]
    ]

    return ScanResult(
        m=comp.m,
        k=comp.k,
        n_max=comp.n_max,
        preperiod=pre,
        period=p,
        p_density=(sum(word) / p if p else None),
        p_residues="{" + ",".join(residues) + "}",
        period_fingerprint=hashlib.sha256(word).hexdigest()[:16],
        max_start_sg=max(comp.start_sg),
        max_state_sg=comp.max_state_sg,
    )


# ---------------------------------------------------------------------------
# Research/mining helpers
# ---------------------------------------------------------------------------

def mine_affine_period_laws(
    results: list[ScanResult],
    max_modulus: int = 12,
    min_points: int = 5,
) -> list[str]:
    """
    Search for exact observed rules:
        period(k) = a*k + b
    separately on k congruence classes modulo q.

    These are CONJECTURE GENERATORS. They are not proofs.
    """
    messages = []

    by_m: dict[int, list[ScanResult]] = {}
    for row in results:
        if row.period is not None:
            by_m.setdefault(row.m, []).append(row)

    for m, rows in sorted(by_m.items()):
        rows = sorted(rows, key=lambda x: x.k)

        for q in range(1, max_modulus + 1):
            for r in range(q):
                group = [x for x in rows if x.k % q == r]
                if len(group) < min_points:
                    continue

                # Need two distinct k values.
                x1, x2 = group[0], group[1]
                if x1.k == x2.k:
                    continue

                a = Fraction(x2.period - x1.period, x2.k - x1.k)
                b = Fraction(x1.period) - a * x1.k

                if all(Fraction(x.period) == a * x.k + b for x in group):
                    # Avoid printing equivalent weaker descriptions repeatedly.
                    if q > 1:
                        # If all k values in the entire m-set obey this same law,
                        # q=1 already captures it.
                        all_rows_obey = all(
                            Fraction(x.period) == a * x.k + b for x in rows
                        )
                        if all_rows_obey:
                            continue

                    a_txt = str(a.numerator) if a.denominator == 1 else str(a)
                    b_txt = (
                        f"+{b.numerator}" if b.denominator == 1 and b >= 0
                        else str(b)
                    )

                    messages.append(
                        f"m={m}, k ≡ {r} (mod {q}), observed for "
                        f"{len(group)} k-values from {group[0].k} to {group[-1].k}: "
                        f"period = ({a_txt})*k {b_txt}"
                    )

    # Remove exact duplicate lines while preserving order.
    seen = set()
    unique = []
    for msg in messages:
        if msg not in seen:
            seen.add(msg)
            unique.append(msg)
    return unique


def unusual_cases(results: list[ScanResult], limit: int = 12) -> list[str]:
    """
    Surface computationally unusual cases. "Unusual" does NOT mean novel.
    """
    scored = []

    # Count period fingerprints so rare signatures can be surfaced.
    fp_count: dict[tuple[int, str], int] = {}
    for r in results:
        if r.period_fingerprint:
            key = (r.m, r.period_fingerprint)
            fp_count[key] = fp_count.get(key, 0) + 1

    for r in results:
        score = 0.0
        reasons = []

        if r.period is None:
            score += 10
            reasons.append("no period detected within search bound")
        else:
            ratio = r.period / max(1, r.k)
            if ratio >= 4:
                score += min(5, ratio / 2)
                reasons.append(f"large period/k ratio ({ratio:.2f})")

            if r.preperiod is not None and r.preperiod >= 4 * r.k:
                score += min(4, r.preperiod / max(1, 4 * r.k))
                reasons.append(f"large preperiod ({r.preperiod})")

            if fp_count.get((r.m, r.period_fingerprint), 0) == 1:
                score += 1
                reasons.append("unique period fingerprint in this scan")

        if reasons:
            scored.append((score, r, "; ".join(reasons)))

    scored.sort(key=lambda x: (-x[0], x[1].m, x[1].k))

    return [
        f"m={r.m}, k={r.k}: {reason}"
        for _, r, reason in scored[:limit]
    ]


def write_scan_outputs(
    out_dir: Path,
    results: list[ScanResult],
    affine_laws: list[str],
    unusual: list[str],
) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    csv_path = out_dir / "scan_results.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        fieldnames = list(asdict(results[0]).keys()) if results else [
            "m", "k", "n_max", "preperiod", "period", "p_density",
            "p_residues", "period_fingerprint", "max_start_sg",
            "max_state_sg", "exact_state_preperiod_upper_bound",
            "exact_state_period",
        ]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in results:
            writer.writerow(asdict(r))

    report_path = out_dir / "research_report.md"
    with report_path.open("w", encoding="utf-8") as f:
        f.write("# Distance-Constrained Subtraction Game Scan\n\n")
        f.write(
            "**Warning:** this report identifies computational patterns only. "
            "It does not establish literature novelty.\n\n"
        )

        f.write("## Candidate affine period laws\n\n")
        if affine_laws:
            for item in affine_laws:
                f.write(f"- {item}\n")
        else:
            f.write("- None found under the current scan settings.\n")

        f.write("\n## Computationally unusual cases\n\n")
        if unusual:
            for item in unusual:
                f.write(f"- {item}\n")
        else:
            f.write("- None surfaced.\n")

        f.write("\n## Novelty checklist for any promising pattern\n\n")
        f.write(
            "1. Re-run the case with at least 5-10x larger n.\n"
            "2. Extend the k range well beyond the discovery range.\n"
            "3. Search for a counterexample before attempting a proof.\n"
            "4. Prove the statement for an infinite family if possible.\n"
            "5. Search the mathematical literature for the exact rule and equivalent formulations.\n"
            "6. Distinguish clearly among proved theorems, finite computational evidence, and conjectures.\n"
        )

        f.write("\n## Suggested literature-search phrases\n\n")
        f.write(
            "- \"repetition-free subtraction game\"\n"
            "- \"dynamic subtraction game previous move\"\n"
            "- \"distance constrained subtraction game\"\n"
            "- \"Sprague-Grundy previous move restriction\"\n"
            "- \"take-away game previous move difference\"\n"
            "- \"subtraction game forbidden consecutive move sizes\"\n"
        )

    terms_path = out_dir / "literature_search_terms.txt"
    terms_path.write_text(
        "\n".join([
            '"repetition-free subtraction game"',
            '"dynamic subtraction game" "previous move"',
            '"distance constrained" "subtraction game"',
            '"Sprague-Grundy" "previous move" subtraction',
            '"take-away game" "previous move" difference',
            '"subtraction game" forbidden consecutive move sizes',
        ]) + "\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_single(args: argparse.Namespace) -> int:
    comp = solve_game(args.k, args.m, args.n)
    result = period_description(comp, args.max_period, args.min_repeats)

    if args.exact_state_cycle:
        exact = detect_exact_full_state_cycle(comp, max_end=args.exact_cycle_max_n)
        if exact:
            result.exact_state_preperiod_upper_bound = exact[0]
            result.exact_state_period = exact[1]

    print(f"D(k={args.k}, m={args.m}), computed through n={args.n}")
    print(f"max starting SG = {result.max_start_sg}")
    print(f"max state SG    = {result.max_state_sg}")

    if result.period is None:
        print("candidate P-period: not detected")
    else:
        print(f"candidate P-preperiod = {result.preperiod}")
        print(f"candidate P-period    = {result.period}")
        print(f"P-density in period   = {result.p_density:.6f}")
        print(f"P residues mod period = {result.p_residues}")
        print(f"period fingerprint    = {result.period_fingerprint}")

    if args.exact_state_cycle:
        if result.exact_state_period is None:
            print("exact full-state cycle: not found within requested range")
        else:
            print(
                "exact full-state cycle: "
                f"period={result.exact_state_period}, "
                f"preperiod <= {result.exact_state_preperiod_upper_bound}"
            )

    print("\nFirst starting P-positions:")
    first_p = [n for n, flag in enumerate(comp.start_p) if flag][: args.show_p]
    print(first_p)

    return 0


def cmd_scan(args: argparse.Namespace) -> int:
    results: list[ScanResult] = []
    total = len(args.m_values) * (args.k_max - args.k_min + 1)
    done = 0

    for m in args.m_values:
        for k in range(args.k_min, args.k_max + 1):
            done += 1
            print(f"[{done}/{total}] computing m={m}, k={k} ...", flush=True)

            comp = solve_game(k, m, args.n)
            result = period_description(comp, args.max_period, args.min_repeats)

            # Exact full-state detection is intentionally optional because it
            # costs more memory/time than P-period detection.
            if args.exact_state_cycle and k <= args.exact_cycle_k_max:
                exact = detect_exact_full_state_cycle(
                    comp,
                    max_end=args.exact_cycle_max_n,
                )
                if exact:
                    result.exact_state_preperiod_upper_bound = exact[0]
                    result.exact_state_period = exact[1]

            results.append(result)

            if result.period is None:
                print("    no candidate P-period found")
            else:
                print(
                    f"    pre={result.preperiod}, p={result.period}, "
                    f"density={result.p_density:.4f}"
                )

            del comp
            gc.collect()

    affine = mine_affine_period_laws(
        results,
        max_modulus=args.max_modulus,
        min_points=args.min_family_points,
    )
    unusual = unusual_cases(results)

    out_dir = Path(args.out)
    write_scan_outputs(out_dir, results, affine, unusual)

    print("\n=== Candidate affine laws ===")
    if affine:
        for law in affine[:50]:
            print("  " + law)
        if len(affine) > 50:
            print(f"  ... plus {len(affine) - 50} more in the report")
    else:
        print("  none found")

    print("\n=== Computationally unusual cases ===")
    if unusual:
        for item in unusual:
            print("  " + item)
    else:
        print("  none surfaced")

    print(f"\nWrote: {out_dir / 'scan_results.csv'}")
    print(f"Wrote: {out_dir / 'research_report.md'}")
    print(f"Wrote: {out_dir / 'literature_search_terms.txt'}")
    return 0


def cmd_test_period_formula(args: argparse.Namespace) -> int:
    """
    Test:
        period(k,m) == a*k + b
    for k in the requested range satisfying k == r (mod q).
    """
    tested = 0

    for k in range(args.k_min, args.k_max + 1):
        if k % args.q != args.r % args.q:
            continue

        expected = args.a * k + args.b
        if expected <= 0:
            print(f"Skipping k={k}: predicted period {expected} is not positive.")
            continue

        tested += 1
        print(f"testing k={k}, m={args.m}; expected p={expected} ...", flush=True)

        comp = solve_game(k, args.m, args.n)
        result = period_description(comp, args.max_period, args.min_repeats)

        if result.period != expected:
            print("\nCOUNTEREXAMPLE / FAILURE OF CURRENT EVIDENCE")
            print(f"  m={args.m}, k={k}")
            print(f"  predicted period = {expected}")
            print(f"  detected period  = {result.period}")
            print(f"  detected preperiod = {result.preperiod}")
            print(
                "\nThis does not automatically prove the formula false if no period "
                "was detected; increase --n and --max-period first."
            )
            return 1

        del comp
        gc.collect()

    print(
        f"\nNo counterexample found among {tested} tested k-values. "
        "This is evidence, not a proof."
    )
    return 0


def cmd_self_test(_: argparse.Namespace) -> int:
    # Test 1: k=1,m=0.
    # After a move of 1, another 1 is forbidden. Starting game alternates:
    # n=0 P, n=1 N, n>=2? first player takes 1, opponent is stuck -> N.
    c = solve_game(1, 0, 8)
    expected = [1, 0, 0, 0, 0, 0, 0, 0, 0]
    assert list(c.start_p) == expected, (list(c.start_p), expected)

    # Test recurrence against a deliberately slow reference implementation
    # over many small parameter triples.
    def slow(k: int, m: int, N: int):
        g = [[0] * (k + 1) for _ in range(N + 1)]
        start = [0] * (N + 1)

        for n in range(1, N + 1):
            vals0 = {g[n-r][r] for r in range(1, min(k, n) + 1)}
            z = 0
            while z in vals0:
                z += 1
            start[n] = z

            for s in range(1, k + 1):
                vals = {
                    g[n-r][r]
                    for r in range(1, min(k, n) + 1)
                    if abs(r - s) > m
                }
                z = 0
                while z in vals:
                    z += 1
                g[n][s] = z
        return g, start

    for k in range(1, 8):
        for m in range(0, 4):
            N = 35
            fast = solve_game(k, m, N)
            slow_g, slow_start = slow(k, m, N)
            stride = k + 1

            assert list(fast.start_sg) == slow_start
            for n in range(N + 1):
                for s in range(1, k + 1):
                    assert fast.table[n * stride + s] == slow_g[n][s]

    print("All self-tests passed.")
    return 0


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Research engine for distance-constrained dynamic subtraction games."
    )
    sub = p.add_subparsers(dest="command", required=True)

    s = sub.add_parser("self-test", help="verify optimized recurrence against a slow solver")
    s.set_defaults(func=cmd_self_test)

    s = sub.add_parser("single", help="analyze one (k,m) game")
    s.add_argument("--k", type=int, required=True)
    s.add_argument("--m", type=int, default=1)
    s.add_argument("--n", type=int, default=50000)
    s.add_argument("--max-period", type=int, default=10000)
    s.add_argument("--min-repeats", type=int, default=12)
    s.add_argument("--show-p", type=int, default=40)
    s.add_argument("--exact-state-cycle", action="store_true")
    s.add_argument(
        "--exact-cycle-max-n",
        type=int,
        default=20000,
        help="maximum n used by full-state cycle search",
    )
    s.set_defaults(func=cmd_single)

    s = sub.add_parser("scan", help="sweep a range of k and m values")
    s.add_argument("--m-values", type=int, nargs="+", default=[1])
    s.add_argument("--k-min", type=int, default=2)
    s.add_argument("--k-max", type=int, default=60)
    s.add_argument("--n", type=int, default=50000)
    s.add_argument("--max-period", type=int, default=10000)
    s.add_argument("--min-repeats", type=int, default=12)
    s.add_argument("--max-modulus", type=int, default=12)
    s.add_argument("--min-family-points", type=int, default=5)
    s.add_argument("--out", default="distance_game_results")
    s.add_argument("--exact-state-cycle", action="store_true")
    s.add_argument("--exact-cycle-k-max", type=int, default=20)
    s.add_argument("--exact-cycle-max-n", type=int, default=10000)
    s.set_defaults(func=cmd_scan)

    s = sub.add_parser(
        "test-period-formula",
        help="try to falsify period(k)=a*k+b on k == r (mod q)",
    )
    s.add_argument("--m", type=int, default=1)
    s.add_argument("--k-min", type=int, required=True)
    s.add_argument("--k-max", type=int, required=True)
    s.add_argument("--n", type=int, default=100000)
    s.add_argument("--a", type=int, required=True)
    s.add_argument("--b", type=int, required=True)
    s.add_argument("--q", type=int, default=1)
    s.add_argument("--r", type=int, default=0)
    s.add_argument("--max-period", type=int, default=25000)
    s.add_argument("--min-repeats", type=int, default=20)
    s.set_defaults(func=cmd_test_period_formula)

    return p


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if hasattr(args, "k_min") and hasattr(args, "k_max"):
        if args.k_min > args.k_max:
            parser.error("--k-min must be <= --k-max")

    if hasattr(args, "q") and args.q <= 0:
        parser.error("--q must be positive")

    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
