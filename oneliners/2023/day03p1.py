print((lambda re, grid: sum(sum(int(match.group()) if any(0 <= cr < len(grid) and 0 <= cc < len(grid[cr]) and grid[cr][cc] not in ".1234567890" for cr in [r - 1, r, r + 1] for cc in range(match.start() - 1, match.end() + 1)) else 0 for match in re.finditer("\\d+", row)) for r, row in enumerate(grid)))(__import__("re"), open(0).read().splitlines()))
