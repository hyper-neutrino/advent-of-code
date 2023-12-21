from collections import deque

grid = open(0).read().splitlines()

sr, sc = next((r, c) for r, row in enumerate(grid) for c, ch in enumerate(row) if ch == "S")

ans = set()
seen = {(sr, sc)}
q = deque([(sr, sc, 64)])

while q:
    r, c, s = q.popleft()

    if s % 2 == 0:
        ans.add((r, c))
    if s == 0:
        continue

    for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if nr < 0 or nr >= len(grid) or nc < 0 or nc >= len(grid[0]) or grid[nr][nc] == "#" or (nr, nc) in seen:
            continue
        seen.add((nr, nc))
        q.append((nr, nc, s - 1))

print(len(ans))