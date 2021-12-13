grid = {}

for line in data.splitlines():
    l, r = line.split(" -> ")
    x1, y1 = map(int, l.split(","))
    x2, y2 = map(int, r.split(","))
    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[(x, y)] = grid.get((x, y), 0) + 1

t = 0
for v in grid.values():
    if v > 1:
        t += 1

print(t)
