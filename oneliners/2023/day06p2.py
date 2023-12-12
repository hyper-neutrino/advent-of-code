print((lambda t, d: (lambda k: int(t - int((t - k ** 0.5) / 2 + 1) * 2 + 1) if k > 0 else 0)(t ** 2 - 4 * d))(*(int(line.split(":")[1].replace(" ", "")) for line in open(0))))
