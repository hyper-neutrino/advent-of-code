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

for i in range(0, len(o), 40):
    for j in range(40):
        print(end = "#" if abs(o[i + j] - j) <= 1 else " ")
        # change to "##" and "  " if you have trouble reading the output
    print()
