pyint = int

def int(x, y = 10):
    return pyint("".join(x), y)

k = list("".join(bin(int(c, 16))[2:].zfill(4) for c in data.strip()))

def parse(k):
    version = int(k[:3], 2)
    k[:] = k[3:]
    typeid = int(k[:3], 2)
    k[:] = k[3:]
    if typeid == 4:
        data = []
        while True:
            cont = k.pop(0)
            data += k[:4]
            k[:] = k[4:]
            if cont == "0": break
        data = int(data, 2)
        return (version, typeid, data)
    else:
        packets = []
        if k.pop(0) == "0":
            length = int(k[:15], 2)
            k[:] = k[15:]
            d = k[:length]
            k[:] = k[length:]
            while d:
                packets.append(parse(d))
        else:
            num = int(k[:11], 2)
            k[:] = k[11:]
            for _ in range(num):
                packets.append(parse(k))
        return (version, typeid, packets)

def vsum(k):
    t = k[0]
    if k[1] == 4:
        return t
    else:
        return t + sum(map(vsum, k[2]))

q = parse(k)

print(vsum(q))
