from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    prev_map = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i
    return


nums = [2, 7, 11, 15]
target = 9
print(two_sum(nums, target))
