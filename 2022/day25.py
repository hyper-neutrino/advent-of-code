total = 0

for line in open(0).read().splitlines():
    coef = 1
    for x in line[::-1]:
        total += ("=-012".find(x) - 2) * coef
        coef *= 5

output = ""

while total:
    rem = total % 5
    total //= 5
    
    if rem <= 2:
        output = str(rem) + output
    else:
        output = "   =-"[rem] + output
        total += 1

print(output)
