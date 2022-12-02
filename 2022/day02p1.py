t = 0

for line in open(0).read().splitlines():
    x, y = line.split()

    x = ord(x) - 65
    y = ord(y) - ord("X")

    if x == y:
        t += 3
    elif (y - x) % 3 == 1:
        t += 6
    
    t += y + 1

print(t)
