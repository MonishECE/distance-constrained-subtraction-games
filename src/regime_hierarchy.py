import sys
sys.path.insert(0, 'src')
from fast_solver import fast_interval_solver


def universal_alive(limit):
    """Compute a(n)=1 iff row n nonempty in the universal game, via the proved recursion.

    Base values are taken from the exact solver at a small k.
    """
    _, starts = fast_interval_solver(64, 1, 64)
    rows, _ = fast_interval_solver(64, 1, 64)
    a = [1 if rows[n] else 0 for n in range(10)]
    a += [0] * (limit + 1 - len(a))
    for n in range(10, limit + 1):
        m = n // 2
        if n % 2 == 0:
            a[n] = 1 - a[m]
        else:
            a[n] = 1 - max(a[m], a[m + 1])
    return a


def runs(a, limit):
    out = []
    cur = None
    for n in range(limit + 1):
        v = a[n]
        if cur and cur[0] == v:
            cur[2] = n
        else:
            if cur:
                out.append(tuple(cur))
            cur = [v, n, n]
    out.append(tuple(cur))
    return out


def template_fail(k, A, n_max):
    _, starts = fast_interval_solver(k, 1, n_max)
    p = 2 * k + A + 2
    r2, r3 = A % p, (k + A + 1) % p
    for n in range(n_max + 1):
        t = n % p
        if starts[n] != ((t == 0) or (t == r2) or (t == r3)):
            return n
    return None


LIMIT = 5000
a = universal_alive(LIMIT)
# verify recursion against solver on a moderate range
_, st = fast_interval_solver(LIMIT, 1, LIMIT)
solver_a = [1 if v else 0 for v in st]
rows, _ = fast_interval_solver(LIMIT, 1, LIMIT)
solver_a = [1 if rows[n] else 0 for n in range(LIMIT + 1)]
assert a[:LIMIT + 1] == solver_a, 'recursion mismatch'
print('universal recursion verified to n =', LIMIT)

r = runs(a, LIMIT)
alive_starts = [x[1] for x in r if x[0] == 1]
print('\nalive run starts up to', LIMIT, ':')
print(alive_starts)
print('\nalive runs:')
for x in r:
    if x[0] == 1:
        print(f'  [{x[1]},{x[2]}] len {x[2]-x[1]+1}')

# For each alive-run start A, find all k<A where T(k,A) holds (n_max generous).
print('\n=== regime ranges per candidate A (scanning k < A) ===')
for A in alive_starts:
    if A < 6 or A > 1200:
        continue
    good = []
    fails = {}
    for k in range(max(1, A // 4), A):
        n_max = 30 * k + 2 * A + 2000
        f = template_fail(k, A, n_max)
        if f is None:
            good.append(k)
        else:
            fails[k] = f
    if good:
        # contiguous ranges
        ranges = []
        s = good[0]
        prev = good[0]
        for k in good[1:]:
            if k == prev + 1:
                prev = k
            else:
                ranges.append((s, prev))
                s = k
                prev = k
        ranges.append((s, prev))
        print(f'A={A}: k-ranges {ranges}')
        for lo, hi in ranges:
            if lo - 1 in fails:
                print(f'    k={lo-1} first failure n={fails[lo-1]}')
            if hi + 1 in fails:
                print(f'    k={hi+1} first failure n={fails[hi+1]}')
    else:
        print(f'A={A}: no k')
