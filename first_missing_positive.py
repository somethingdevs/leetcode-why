from typing import List


def first_missing_positive(nums: List[int]) -> int:
    new = set(nums)
    i = 1
    while i in new:
        i += 1
    return i

print(first_missing_positive([1, 2, 0]))
