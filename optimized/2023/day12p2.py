from functools import lru_cache

answer = 0

for line in open(0):
    cfg, nums = line.split()
    nums = tuple(map(int, nums.split(",")))
    
    cfg = "?".join([cfg] * 5)
    nums *= 5
    
    cl = len(cfg)

    @lru_cache
    def calc(ci, ni):
        if ci >= cl:
            return 1 if ni >= len(nums) else 0

        if ni >= len(nums):
            return 0 if "#" in cfg[ci:] else 1
        
        total = 0
        
        if cfg[ci] != ".":
            if nums[ni] <= cl - ci and "." not in cfg[ci:ci + nums[ni]] and (nums[ni] == cl - ci or cfg[ci + nums[ni]] != "#"):
                total += calc(ci + nums[ni] + 1, ni + 1)
        
        if cfg[ci] != "#":
            total += calc(ci + 1, ni)
            
        return total
        
    answer += calc(0, 0)

print(answer)