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
    for dx in range(1, maxx):
        x = 0
        for _ in range(step):
            x += dx
            if dx > 0:
                dx -= 1
        if minx <= x <= maxx:
            return True
    return False

dy = -miny

while True:
    if any(can_land_dx(step) for step in steps_for_dy(dy)):
        print(sum(range(1, dy + 1)))
        break
    dy -= 1
