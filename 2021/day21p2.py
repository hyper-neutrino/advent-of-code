p = list(map(int, data.split()))

cache = {}

def c():
    return [x + y + z for x in [1, 2, 3] for y in [1, 2, 3] for z in [1, 2, 3]]

def u(p0, p1, s0 = 0, s1 = 0):
    k = (p0, p1, s0, s1)
    if k in cache:
        return cache[k]
    oc = [0, 0]
    for r in c():
        p0_ = p0 + r
        p0_ = (p0_ - 1) % 10 + 1
        s0_ = s0 + p0_
        if s0_ >= 21:
            oc[0] += 1
        else:
            dy, dx = u(p1, p0_, s1, s0_)
            oc[0] += dx
            oc[1] += dy
    cache[k] = oc
    return oc

print(max(u(*p)))
