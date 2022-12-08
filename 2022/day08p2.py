grid = [list(map(int, line)) for line in open(0).read().splitlines()]

t = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        k = grid[r][c]
        L = R = U = D = 0
        for x in range(c - 1, -1, -1):
            L += 1
            if grid[r][x] >= k:
                break
        for x in range(c + 1, len(grid[r])):
            R += 1
            if grid[r][x] >= k:
                break
        for x in range(r - 1, -1, -1):
            U += 1
            if grid[x][c] >= k:
                break
        for x in range(r + 1, len(grid)):
            D += 1
            if grid[x][c] >= k:
                break
        t = max(t, U * D * L * R)

print(t)
