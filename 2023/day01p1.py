t = 0

for x in open(0):
    digits = [ch for ch in x if ch.isdigit()]
    t += int(digits[0] + digits[-1])

print(t)
