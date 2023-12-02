_risk = [list(map(int, line)) for line in lines]

def wrap(x):
    return (x - 1) % 9 + 1

risk = [[0] * len(row) * 5 for row in _risk * 5]

r = len(_risk)
c = len(_risk[0])

for i in range(len(risk)):
    for j in range(len(risk[i])):
        risk[i][j] = wrap(_risk[i % r][j % c] + i // r + j // c)

import heapq

paths = [(0, 0, 0)]

vis = [[0] * len(row) for row in risk]

while True:
    rf, x, y = heapq.heappop(paths)
    if vis[x][y]: continue
    if (x, y) == (len(risk) - 1, len(risk[x]) - 1):
        print(rf)
        exit(0)
    vis[x][y] = 1
    for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if not len(risk) > nx >= 0 <= ny < len(risk[0]): continue
        if vis[nx][ny]: continue
        heapq.heappush(paths, (rf + risk[nx][ny], nx, ny))
