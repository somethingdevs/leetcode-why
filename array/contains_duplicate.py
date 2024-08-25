from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    seen = {}

    for num in nums:
        if num in seen:
            return True
        seen[num] = True

    return False


print(containsDuplicate([1, 2, 3, 1]))
