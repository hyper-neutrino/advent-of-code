t = 0

for k in lines:
    a, b = k.split(" | ")
    for j in b.split():
        if len(j) in [2, 3, 4, 7]:
            t += 1

print(t)
