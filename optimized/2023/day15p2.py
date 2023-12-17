def hash(s):
    val = 0
    for ch in s:
        val = (val + ord(ch)) * 17 % 256
    return val

boxes = [{} for _ in range(256)]

for item in input().split(","):
    if item[-1] == "-":
        label = item[:-1]
        boxes[hash(label)].pop(label, None)
    else:
        label = item[:-2]
        focus = int(item[-1])
        boxes[hash(label)][label] = focus
        
total = 0        

for i, box in enumerate(boxes, 1):
    for j, focus in enumerate(box.values(), 1):
        total += i * j * focus

print(total)