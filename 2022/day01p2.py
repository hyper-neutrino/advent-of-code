a = [0]

while True:
    try:
        line = input()
    except:
        break

    if line == "":
        a.append(0)
        continue

    a[-1] += int(line)

a.sort()
print(sum(a[-3:])
