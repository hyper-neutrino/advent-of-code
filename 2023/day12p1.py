def count(cfg, nums, flag=False):
    if cfg == "":
        return 1 if sum(nums) == 0 else 0

    if sum(nums) == 0:
        return 0 if "#" in cfg else 1
    
    if cfg[0] == "#":
        if flag and nums[0] == 0:
            return 0
        return count(cfg[1:], (nums[0] - 1, *nums[1:]), True)
    
    if cfg[0] == ".":
        if flag and nums[0] > 0:
            return 0
        return count(cfg[1:], nums[1:] if nums[0] == 0 else nums, False)
    
    if flag:
        if nums[0] == 0:
            return count(cfg[1:], nums[1:], False)
        return count(cfg[1:], (nums[0] - 1, *nums[1:]), True)
    
    return count(cfg[1:], nums, False) + count(cfg[1:], (nums[0] - 1, *nums[1:]), True)

total = 0

for line in open(0):
    cfg, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    total += count(cfg, nums)

print(total)