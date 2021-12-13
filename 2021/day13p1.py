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
    break

print(len(dots))
