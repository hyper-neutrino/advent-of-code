grids = [block.splitlines() for block in open(0).read().split("\n\n")]

def to_bin(array):
    return sum(2 ** i if ch == "#" else 0 for i, ch in enumerate(array))

def find_mirror(nums):
    for i in range(1, len(nums)):
        original = i
        j = i - 1
        error = False
        while i < len(nums) and j >= 0:
            if nums[i] != nums[j]:
                if error:
                    break
                diff = nums[i] ^ nums[j]
                if diff & (diff - 1) == 0:
                    error = True
                else:
                    break
            i += 1
            j -= 1
        else:
            if error:
                return original
        
    return 0

total = 0

for grid in grids:
    rows = list(map(to_bin, grid))
    cols = list(map(to_bin, zip(*grid)))
    
    total += 100 * find_mirror(rows) or find_mirror(cols)

print(total)