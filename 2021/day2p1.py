h = v = 0

for k in data.splitlines():
    a, b = k.split()
    b = int(b)
    if a == "forward":
        h += b
    elif a == "down":
        v -= b
    else:
        v += b

print(abs(h) * abs(v))
