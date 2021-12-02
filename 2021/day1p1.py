q = [*map(int, data.split())]

print(sum(y > x for x, y in zip(q, q[1:])))
