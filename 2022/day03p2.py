t = 0

while True:
    try:
        x = input()
        y = input()
        z = input()
    except:
        break

    k, = set(x) & set(y) & set(z)
    if k >= "a":
        t += ord(k) - ord("a") + 1
    else:
        t += ord(k) - ord("A") + 27

print(t)
