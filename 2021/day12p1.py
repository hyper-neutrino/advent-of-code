edges = {}

for line in lines:
    a, b = line.split("-")
    edges[a] = edges.get(a, []) + [b]
    edges[b] = edges.get(b, []) + [a]

def count(node, visited = set()):
    if node == "end":
        return 1
    total = 0
    for next in edges[node]:
        if next in visited: continue
        total += count(next, visited | {node} if node == node.lower() else visited)
    return total

print(count("start"))
