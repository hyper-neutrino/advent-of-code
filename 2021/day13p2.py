dots = set()

t, b = data.split("\r\n\r\n")

for line in t.splitlines():
    x, y = map(int, line.split(","))
    dots.add((x, y))

for line in b.splitlines():
    line = line[11:]
    type, num = line.split("=")
    num = int(num)
    if type == "x":
        dots = {(x if x < num else num - (x - num), y) for x, y in dots}
    else:
        dots = {(x, y if y < num else num - (y - num)) for x, y in dots}

mx = min(x for x, y in dots)
my = min(y for x, y in dots)

dots = {(x - mx, y - my) for x, y in dots}

mx = max(x for x, y in dots)
my = max(y for x, y in dots)

g = [["  "] * (mx + 1) for _ in range(my + 1)]

for x, y in dots:
    g[y][x] = "##"

for r in g:
    print("".join(r))
