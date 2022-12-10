x = 1

o = []

for line in open(0):
    if line == "noop\n":
        o.append(x)
    else:
        v = int(line.split()[1])
        o.append(x)
        o.append(x)
        x += v

print(sum(x * y + y for x, y in list(enumerate(o))[19::40]))
