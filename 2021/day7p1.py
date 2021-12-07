k = list(map(int, data.split(",")))

q = float("inf")

for i in range(min(k), max(k) + 1):
    t = sum(abs(x - i) for x in k)
    q = min(q, t)

print(q)
