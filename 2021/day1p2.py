q = [*map(int, data.split())]
r = [x + y + z for x, y, z in zip(q, q[1:], q[2:])]

print(sum(y > x for x, y in zip(r, r[1:])))
