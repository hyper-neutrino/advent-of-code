steps, _, *rest = open(0).read().splitlines()

network = {}

for line in rest:
    pos, targets = line.split(" = ")
    network[pos] = targets[1:-1].split(", ")

step_count = 0
current = "AAA"

while current != "ZZZ":
    step_count += 1
    current = network[current][0 if steps[0] == "L" else 1]
    steps = steps[1:] + steps[0]

print(step_count)