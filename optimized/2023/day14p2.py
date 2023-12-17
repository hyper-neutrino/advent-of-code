grid = tuple(open(0).read().splitlines())

def cycle():
    global grid
    for _ in range(4):
        grid = list(zip(*grid))
        grid = ["#".join("".join(sorted(block, reverse=True)) for block in "".join(row).split("#")) for row in grid]
        grid = tuple(row[::-1] for row in grid)

states = []
seen = set()
index = 0

while grid not in seen:
    states.append(grid)
    seen.add(grid)
    cycle()
    index += 1
    
offset = states.index(grid)
cycle_length = index - offset

grid = states[(1_000_000_000 - offset) % cycle_length + offset]

L = len(grid)
print(sum(row.count("O") * (L - r) for r, row in enumerate(grid)))