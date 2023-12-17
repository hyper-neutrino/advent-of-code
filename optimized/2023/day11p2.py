grid = open(0).read().splitlines()

scale = 1000000

def construct_psa(grid):
    psa = [0 for _ in range(len(grid) + 1)]
    for i, row in enumerate(grid):
        psa[i] = psa[i - 1] + (scale if all(x == "." for x in row) else 1)
    return psa

row_psa = construct_psa(grid)
col_psa = construct_psa(list(zip(*grid)))

rows = []
cols = []

for r, row in enumerate(grid):
    count = row.count("#")
    if count > 0:
        rows.append((r, count))
        
for c, col in enumerate(zip(*grid)):
    count = col.count("#")
    if count > 0:
        cols.append((c, count))

total = 0

def compute(indexes, psa):
    global total
    cumulative = 0
    num_seen = 0
    for index, count in indexes:
        total += (num_seen * psa[index] - cumulative) * count
        cumulative += psa[index] * count
        num_seen += count

compute(rows, row_psa)
compute(cols, col_psa)

print(total)