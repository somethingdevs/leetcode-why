from typing import List


def missingNumber(nums: List[int]) -> int:
    sorted_nums = sorted(nums)

    for i in range(len(nums)+1):
        if sorted_nums[i] != i:
            return i

    return len(nums) # Edge case - Missing number is last one

nums = [9,6,4,2,3,5,7,0,1]
print(missingNumber(nums))