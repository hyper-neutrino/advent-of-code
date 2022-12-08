grid = [list(map(int, line)) for line in open(0).read().splitlines()]

t = 0

for r in range(len(grid)):
    for c in range(len(grid[r])):
        k = grid[r][c]
        if all(grid[r][x] < k for x in range(c)) or all(grid[r][x] < k for x in range(c + 1, len(grid[r]))) or all(grid[x][c] < k for x in range(r)) or all(grid[x][c] < k for x in range(r + 1, len(grid))):
            t += 1

print(t)
