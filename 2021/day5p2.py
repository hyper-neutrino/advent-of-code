grid = {}

for line in data.splitlines():
    l, r = line.split(" -> ")
    x1, y1 = map(int, l.split(","))
    x2, y2 = map(int, r.split(","))
    dx = x2 - x1
    dy = y2 - y1
    if dx: dx = dx // abs(dx)
    if dy: dy = dy // abs(dy)
    x = x1
    y = y1
    while True:
        grid[(x, y)] = grid.get((x, y), 0) + 1
        if x == x2 and y == y2:
            break
        x += dx
        y += dy

t = 0
for v in grid.values():
    if v > 1:
        t += 1

print(t)
