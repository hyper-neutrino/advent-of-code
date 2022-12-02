t = 0

for line in open(0).read().splitlines():
    x, y = line.split()

    x = ord(x) - 65

    if y == "X":
        t += (x - 1) % 3 + 1
    elif y == "Y":
        t += 3 + x + 1
    else:
        t += 6 + (x + 1) % 3 + 1

print(t)
