grid = list(map(list, lines))
east = set()
south = set()

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == ">":
            east.add((i, j))
        elif grid[i][j] == "v":
            south.add((i, j))

def pp(e, s):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) in e:
                print(end = ">")
            elif (i, j) in s:
                print(end = "v")
            else:
                print(end = ".")
        print()

i = 0

while True:
    ne = set()
    ns = set()
    all = east | south
    for r, c in east:
        n = (r, (c + 1) % len(grid[0]))
        if n in all:
            ne.add((r, c))
        else:
            ne.add(n)
    t = east == ne
    east = ne
    all = east | south
    for r, c in south:
        n = ((r + 1) % len(grid), c)
        if n in all:
            ns.add((r, c))
        else:
            ns.add(n)
    if t and south == ns:
        break
    south = ns
    i += 1

print(i)
