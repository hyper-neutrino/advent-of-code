print((lambda h: sum(map(h, input().split(","))))(lambda s: sum(17 ** i * ord(ch) % 256 for i, ch in enumerate(s[::-1], 1)) % 256))
