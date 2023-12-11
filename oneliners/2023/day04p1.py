print(sum(int(2 ** (len(x & y) - 1)) for x, y in [[set(group.split()) for group in line.split(":")[1].strip().split(" | ")] for line in open(0)]))
