import math
from collections import deque

blizzards = tuple(set() for _ in range(4))

for r, line in enumerate(open(0).read().splitlines()[1:]):
    for c, item in enumerate(line[1:]):
        if item in "<>^v":
            blizzards["<>^v".find(item)].add((r, c))

queue = deque([(0, -1, 0)])
seen = set()
target = (r, c - 1)

lcm = r * c // math.gcd(r, c)

while queue:
    time, cr, cc = queue.popleft()
    
    time += 1

    for dr, dc in ((0, 1), (0, -1), (-1, 0), (1, 0), (0, 0)):
        nr = cr + dr
        nc = cc + dc

        if (nr, nc) == target:
            print(time)
            exit(0)
        
        if (nr < 0 or nc < 0 or nr >= r or nc >= c) and not (nr, nc) == (-1, 0):
            continue

        fail = False

        if (nr, nc) != (-1, 0):
            for i, tr, tc in ((0, 0, -1), (1, 0, 1), (2, -1, 0), (3, 1, 0)):
                if ((nr - tr * time) % r, (nc - tc * time) % c) in blizzards[i]:
                    fail = True
                    break

        if not fail:
            key = (nr, nc, time % lcm)
            
            if key in seen:
                continue

            seen.add(key)
            queue.append((time, nr, nc))
