def hash(s):
    v = 0
    
    for ch in s:
        v += ord(ch)
        v *= 17
        v %= 256

    return v

print(sum(map(hash, input().split(","))))