from collections import deque

lines = [[int(x) for x in r] for r in lines]

g = [[0] * len(r) for r in lines]

T = 1

for r in range(len(lines)):
    for c in range(len(lines[r])):
        if lines[r][c] == 9 or g[r][c] != 0: continue
        vis = {(r, c)}
        q = deque()
        q.append((r, c))
        while q:
            r, c = q.popleft()
            g[r][c] = T
            for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                if (i, j) in vis: continue
                if 0 <= i < len(lines) and 0 <= j < len(lines[i]):
                    if lines[i][j] != 9:
                        vis.add((i, j))
                        q.append((i, j))
        T += 1

p = sum(g, [])
c = [0] * T

for x in p:
    c[x] += 1

c = c[1:]
c.sort()

print(c[-3] * c[-2] * c[-1])
