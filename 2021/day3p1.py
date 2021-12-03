b = list(map(list, data.splitlines()))

z = list(map(list, zip(*b)))
i = ("".join(max(k, key = k.count) for k in z))
j = ("".join(min(k, key = k.count) for k in z))
print(int(i, 2) * int(j, 2))
