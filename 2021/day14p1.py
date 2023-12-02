s = lines[0]

k = {}

for q in lines[2:]:
    x, y = q.split(" -> ")
    k[x] = y

for _ in range(10):
    n = s[0]
    for c in s[1:]:
        n += k[n[-1] + c]
        n += c
    s = n

c = {}

for char in s:
    if char not in c: c[char] = 0
    c[char] += 1

print(max(c.values()) - min(c.values()))
