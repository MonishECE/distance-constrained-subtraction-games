import sys
sys.path.insert(0, 'src')
from fast_solver import fast_interval_solver

LIMIT = 2_000_000
# base values from exact solver
rows, _ = fast_interval_solver(64, 1, 64)
a = bytearray(LIMIT + 1)
for n in range(10):
    a[n] = 1 if rows[n] else 0
for n in range(10, LIMIT + 1):
    m = n >> 1
    if n & 1:
        a[n] = 1 - (a[m] | a[m + 1])
    else:
        a[n] = 1 - a[m]

runs = []
cur_val = a[0]
cur_start = 0
for n in range(1, LIMIT + 1):
    if a[n] != cur_val:
        runs.append((cur_val, cur_start, n - 1))
        cur_val = a[n]
        cur_start = n
runs.append((cur_val, cur_start, LIMIT))

alive_starts = [s for v, s, e in runs if v == 1]
print('alive run starts (first 30):', alive_starts[:30])
incs = [alive_starts[i+1] - alive_starts[i] for i in range(len(alive_starts)-1)]
print('increments (first 40):', incs[:40])

# check pattern 2^j, 2^j, 3*2^j for j odd >= 3 after the initial 6,2,6
ok = True
j = 3
i = 3  # incs[0],incs[1],incs[2] = 6,2,6
while i + 2 < len(incs):
    p = 1 << j
    expect = [p, p, 3 * p]
    if incs[i:i+3] != expect:
        print(f'pattern break at inc index {i} (j={j}): got {incs[i:i+3]} expected {expect}')
        ok = False
        break
    i += 3
    j += 2
print('pattern holds to index', i, 'j=', j, 'ok=', ok)

# alive run lengths and gap lengths
print('\nlast alive runs:')
for v, s, e in runs[-8:]:
    if v == 1:
        print(f'  [{s},{e}] len {e-s+1}')
