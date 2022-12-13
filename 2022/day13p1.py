x = list(map(str.splitlines, open(0).read().strip().split("\n\n")))

def f(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return f([x], y)
    else:
        if type(y) == int:
            return f(x, [y])
    
    for a, b in zip(x, y):
        v = f(a, b)
        if v:
            return v
    
    return len(x) - len(y)

t = 0

for i, (a, b) in enumerate(x):
    if f(eval(a), eval(b)) < 0:
        t += i + 1

print(t)
