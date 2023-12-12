print(sum((lambda f: f(f, list(map(int, line.split()))))(lambda f, a: 0 if set(a) == {0} else a[-1] + f(f, [y - x for x, y in zip(a, a[1:])])) for line in open(0)))
