monkeys = {}

x = [line.strip() for line in open(0)]

for a in x:
    name, expr = a.split(": ")
    if expr.isdigit():
        monkeys[name] = int(expr)
    else:
        left, op, right = expr.split()
        if left in monkeys and right in monkeys:
            monkeys[name] = eval(f"{monkeys[left]} {op} {monkeys[right]}")
        else:
            x.append(a)

print(monkeys["root"])