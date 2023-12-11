print(sum(m["blue"] * m["green"] * m["red"] for m in (dict(sorted((y, int(x)) for x, y in map(str.split, line.split(":")[1].strip().replace(";", ",").split(", ")))) for line in open(0))))
