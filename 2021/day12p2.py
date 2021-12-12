edges = {}

for line in lines:
    a, b = line.split("-")
    edges[a] = edges.get(a, []) + [b]
    edges[b] = edges.get(b, []) + [a]

def count(node, visited = set(), doubled = False):
    if node == "end":
        return 1
    total = 0
    for next in edges[node]:
        if next == "start": continue
        if next in visited and doubled: continue
        if next in visited:
            total += count(next, visited | {node} if node == node.lower() else visited, True)
        else:
            total += count(next, visited | {node} if node == node.lower() else visited, doubled)
    return total

print(count("start"))
