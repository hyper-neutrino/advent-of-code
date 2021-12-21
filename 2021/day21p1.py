p = list(map(int, data.split()))
pid = 1

rolls = 0

def roll():
    global rolls
    rolls += 1
    return (rolls - 1) % 100 + 1

ps = [0, 0]

while True:
    pid ^= 1
    p[pid] += roll() + roll() + roll()
    p[pid] = (p[pid] - 1) % 10 + 1
    ps[pid] += p[pid]
    if ps[pid] >= 1000:
        print(rolls * ps[1 - pid])
        break
