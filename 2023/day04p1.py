t = 0

for x in open(0):
    x = x.split(":")[1].strip()
    a, b = [list(map(int, k.split())) for k in x.split(" | ")]
    j = sum(q in a for q in b)
    if j > 0:
        t += 2 ** (j - 1)

print(t)
