grid = [list(map(int, line)) for line in lines]

print(grid)

f = 0

def flash(grid, r, c):
    global f
    f += 1
    for i in range(r - 1, r + 2):
        for j in range(c - 1, c + 2):
            if i == r and j == c: continue
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]):
                grid[i][j] += 1
                if grid[i][j] == 10:
                    flash(grid, i, j)
                    grid[i][j] += 1

def step(grid):
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            grid[r][c] += 1
            if grid[r][c] == 10:
                flash(grid, r, c)
                grid[r][c] += 1
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] > 9:
                grid[r][c] = 0

for _ in range(100):
    step(grid)

print(f)
