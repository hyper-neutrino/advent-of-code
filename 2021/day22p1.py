on = set()

def gr(q):
    x, y = map(int, q.split(".."))
    return range(max(x, -50), min(y, 50) + 1)

for line in lines:
    ins, data = line.split()
    if ins == "on":
        f = on.add
    else:
        f = on.discard
    xd, yd, zd = [k[2:] for k in data.split(",")]
    for x in gr(xd):
        for y in gr(yd):
            for z in gr(zd):
                f((x, y, z))

print(len(on))
