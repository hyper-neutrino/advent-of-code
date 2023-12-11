print(sum(int(digits[0] + digits[-1]) for digits in [[char for char in line if char.isdigit()] for line in open(0)]))
