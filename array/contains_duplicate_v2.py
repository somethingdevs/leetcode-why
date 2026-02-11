# Using sort, O(n) - if you don't consider the sort
from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    nums = sorted(nums)
    for i in range(len(nums) - 1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Using hashmap, O(n)
def containsDuplicate(nums: List[int]) -> bool:
    seen = {}
    for index, value in enumerate(nums):
        if value in seen:
            return True
        seen[value] = True
    return False

# Using set, O(n) - basically checking if the set already contains the value which means that it was entered; therefore the
def containsDuplicate(nums: List[int]) -> bool:
    seen = set()
    for index, value in enumerate(nums):
        if value in seen:
            return True
        seen.add(value)
    return False

print(containsDuplicate([1, 2, 3, 1]))
