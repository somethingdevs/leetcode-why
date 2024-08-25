from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    longest = 0

    for n in nums:

        if (n - 1) not in nums_set:
            length = 0
            while (n + length) in nums_set:
                length += 1

            longest = max(length, longest)

    return longest


nums = [100, 4, 200, 1, 3, 2]
print(longestConsecutive(nums=nums))
