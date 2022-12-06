line = input()

for x in range(4, len(line)):
    if len(set(line[x - 4:x])) == 4:
        print(x)
        exit(0)
