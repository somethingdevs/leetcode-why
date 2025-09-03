from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    seen = {}

    for num in nums:
        if num in seen:
            return True
        seen[num] = True

    return False


# Solution using sorting
def containsDuplicate(nums: List[int]) -> bool:
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


print(containsDuplicate([1, 2, 3, 1]))
