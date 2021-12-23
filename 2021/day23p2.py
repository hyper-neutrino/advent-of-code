rooms = [*map(list, data.split())]

start = [0, ["."] * 11, rooms]

costs = {"A": 1, "B": 10, "C": 100, "D": 1000}


def steps(state):
    res = []
    # move an amphipod out
    for x, (i, room) in zip([2, 4, 6, 8], enumerate(state[2])):
        if not room:
            continue
        cost = costs[room[-1]] * (5 - len(room))
        q = []
        for nx in range(x, 11):
            if state[1][nx] != ".":
                break
            q.append(nx)
        for nx in range(x - 1, -1, -1):
            if state[1][nx] != ".":
                break
            q.append(nx)
        for j in q:
            if j in [2, 4, 6, 8]:
                continue
            nh = state[1][:]
            nh[j] = room[-1]
            nr = [r[:] for r in state[2]]
            nr[i].pop()
            res.append([state[0] + cost + costs[room[-1]] * abs(j - x), nh, nr])
    # move an amphipod sideways / in
    for i in range(11):
        if state[1][i] == ".":
            continue
        q = []
        for j in range(i + 1, 11):
            if state[1][j] != ".":
                break
            q.append(j)
        for j in range(i - 1, -1, -1):
            if state[1][j] != ".":
                break
            q.append(j)
        for j in q:
            if j in [2, 4, 6, 8]:
                ind = "ABCD".find(state[1][i])
                if (ind + 1) * 2 == j:
                    if all(x == state[1][i] for x in state[2][ind]):
                        nh = state[1][:]
                        nh[i] = "."
                        nr = [r[:] for r in state[2]]
                        nr[ind].append(state[1][i])
                        res.append(
                            [
                                state[0]
                                + costs[state[1][i]]
                                * (abs(i - j) + 5 - len(nr[ind])),
                                nh,
                                nr,
                            ]
                        )
    return res


import heapq

pq = [start]
vis = set()


def c(state):
    return (tuple(state[1]), tuple(map(tuple, state[2])))


end = [[x] * 4 for x in "ABCD"]

while pq:
    state = heapq.heappop(pq)
    cs = c(state)
    if cs in vis:
        continue
    vis.add(cs)
    if state[2] == end:
        print(state[0])
        break
    for k in steps(state):
        if c(k) in vis:
            continue
        heapq.heappush(pq, k)
