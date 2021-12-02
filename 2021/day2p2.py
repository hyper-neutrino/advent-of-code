h = v = a = 0

for k in data.splitlines():
    x, b = k.split()
    b = int(b)
    if x == "forward":
        h += b
        v += a * b
    elif x == "down":
        a -= b
    else:
        a += b

print(abs(h) * abs(v))
