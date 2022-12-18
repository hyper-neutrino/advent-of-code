faces = {}

offsets = [(0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0)]

for line in open(0):
    x, y, z = map(int, line.split(","))
    
    for dx, dy, dz in offsets:
        k = (x + dx, y + dy, z + dz)
        if k not in faces:
            faces[k] = 0
        faces[k] += 1

print(list(faces.values()).count(1))
