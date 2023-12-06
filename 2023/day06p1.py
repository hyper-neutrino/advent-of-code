times, distances = [list(map(int, line.split(":")[1].split())) for line in open(0)]

n = 1

for time, distance in zip(times, distances):
    margin = 0
    for hold in range(time):
        if hold * (time - hold) > distance:
            margin += 1
    n *= margin

print(n)
