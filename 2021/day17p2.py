import re

minx, maxx, miny, maxy = map(int, re.findall(r"-?\d+", data))

def steps_for_dy(dy):
    y = 0
    steps = 0
    valid = []
    while y >= miny:
        if miny <= y <= maxy:
            valid.append(steps)
        y += dy
        dy -= 1
        steps += 1
    return valid

def can_land_dx(step):
    total = set()
    for dx in range(0, maxx + 1):
        x = 0
        odx = dx
        for _ in range(step):
            x += dx
            if dx > 0:
                dx -= 1
        if minx <= x <= maxx:
            total.add(odx)
    return total

total = 0

for dy in range(miny - 1, -miny + 1):
    iter = set()
    for step in steps_for_dy(dy):
        iter |= can_land_dx(step)
    total += len(iter)

print(total)
