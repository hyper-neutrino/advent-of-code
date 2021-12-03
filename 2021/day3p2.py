b = list(map(list, data.splitlines()))

z = list(map(list, zip(*b)))

def cut(items, criteria, index = 0):
    v = [item[index] for item in items]
    q = criteria(v, key = lambda x: (v.count(x), x))
    items = [item for item in items if item[index] == q]
    if len(items) == 1:
        return items[0]
    else:
        return cut(items, criteria, index + 1)

ox = int("".join(cut(b, max)), 2)
co = int("".join(cut(b, min)), 2)

print(ox * co)
