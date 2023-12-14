grid = open(0).read().splitlines()
grid = list(map("".join, zip(*grid)))
grid = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in grid]
grid = list(map("".join, zip(*grid)))

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))