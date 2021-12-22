ranges = []

for line in lines:
    _, d = line.split()
    ranges.append([list(map(int, u[2:].split(".."))) for u in d.split(",")])
    for i in range(3):
        ranges[-1][i][1] += 1

sd = [set() for _ in range(3)]

for i in range(3):
    for r in ranges:
        sd[i].add(r[i][0])
        sd[i].add(r[i][1])

sd = list(map(sorted, sd))

xm = {x: i for i, x in enumerate(sd[0])}
ym = {y: i for i, y in enumerate(sd[1])}
zm = {z: i for i, z in enumerate(sd[2])}

grid = [[[0] * (len(sd[2]) - 1) for _ in range(len(sd[1]) - 1)] for _ in range(len(sd[0]) - 1)]

t = len(ranges)
for i, (k, data) in enumerate(zip(lines, ranges)):
    v = k.split()[0] == "on"
    for x in range(xm[data[0][0]], xm[data[0][1]]):
        for y in range(ym[data[1][0]], ym[data[1][1]]):
            for z in range(zm[data[2][0]], zm[data[2][1]]):
                grid[x][y][z] = v

t = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        for z in range(len(grid[x][y])):
            if grid[x][y][z]:
                t += (sd[0][x + 1] - sd[0][x]) * (sd[1][y + 1] - sd[1][y]) * (sd[2][z + 1] - sd[2][z])

print(t)
