points = [(0, 0)]
dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

b = 0

for line in open(0):
    d, n, _ = line.split()
    dr, dc = dirs[d]
    n = int(n)
    b += n
    r, c = points[-1]
    points.append((r + dr * n, c + dc * n))

A = abs(sum(points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1]) for i in range(len(points)))) // 2
i = A - b // 2 + 1

print(i + b)