grid = open(0).read().splitlines()

total = 0

for col in zip(*grid):
    blocks = "".join(col).split("#")
    index = len(grid) + 1
    for block in blocks:
        n = block.count("O")
        if n > 0:
            total += n * index - n * (n + 1) // 2
        index -= len(block) + 1

print(total)