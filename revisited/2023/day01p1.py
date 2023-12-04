import re

total = 0

n = "one two three four five six seven eight nine".split()
pattern = "\\d|" + "|".join(n)

m = {}
for i, s in enumerate(n, 1):
    m[s] = str(i)

for line in open(0):
    f = re.search(pattern, line).group()
    l = re.search(".*(" + pattern + ")", line).group(1)
    total += int(m.get(f, f) + m.get(l, l))

print(total)