b = set()

abyss = 0

for line in open(0):
    x = [list(map(int, p.split(","))) for p in line.strip().split(" -> ")]
    for (x1, y1), (x2, y2) in zip(x, x[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                b.add(x + y * 1j)
                abyss = max(abyss, y + 1) # This can be moved out of the loops for efficiency; see https://www.youtube.com/watch?v=Uf_IF_3RbKw&lc=UgzeJ55datIEW1jUXrJ4AaABAg

t = 0

while True:
    s = 500
    while True:
        if s.imag >= abyss:
            print(t)
            exit(0)
        if s + 1j not in b:
            s += 1j
            continue
        if s + 1j - 1 not in b:
            s += 1j - 1
            continue
        if s + 1j + 1 not in b:
            s += 1j + 1
            continue
        b.add(s)
        t += 1
        break
