from typing import List


def longestOnes(nums: List[int], k: int) -> int:
    zero_count = 0
    start = 0
    max_length = 0

    for end, n in enumerate(nums):
        if nums[end] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[start] == 0:
                zero_count -= 1
            start += 1

        max_length = max(max_length, end - start + 1)
    return max_length


nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longestOnes(nums, k))
