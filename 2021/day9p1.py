t = 0

for r in range(len(lines)):
    for c in range(len(lines[r])):
        v = []
        for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if 0 <= i < len(lines) and 0 <= j < len(lines[r]):
                v.append(int(lines[i][j]))
        k = int(lines[r][c])
        if k < min(v):
            t += 1 + k

print(t)
