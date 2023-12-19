print(sum(sum(i for i, ch in enumerate("#".join("".join(sorted(segment, reverse=True)) for segment in "".join(col).split("#"))[::-1], 1) if ch == "O") for col in zip(*open(0))))
