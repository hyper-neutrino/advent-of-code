from collections import deque

grid = [list(map(int, line.strip())) for line in open(0)]

buckets = deque([[(0, 0, 0, 0, 1, 0), (0, 0, 0, 1, 0, 0)], *[[] for _ in range(8)]])

seen = {(0, 0, 0, 1, 0): 0, (0, 0, 1, 0, 0): 0}

target = (len(grid) - 1, len(grid[0]) - 1)

while buckets:
    buckets.append([])
    for hl, r, c, dr, dc, n in buckets.popleft():
        if (r, c) == target:
            print(hl)
            exit(0)

        key = (r, c, dr, dc, n)
        if hl > seen[key]:
            continue
        
        dirs = []

        if n < 3:
            dirs.append((dr, dc))

        dirs.append((-dc, dr))
        dirs.append((dc, -dr))
        
        for ndr, ndc in dirs:
            nr = r + ndr
            nc = c + ndc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]):
                nhl = hl + grid[nr][nc]
                key = (nr, nc, ndr, ndc, n + 1 if (ndr, ndc) == (dr, dc) else 1)
                if key not in seen or nhl < seen[key]:
                    seen[key] = nhl
                    buckets[grid[nr][nc] - 1].append((nhl, *key))