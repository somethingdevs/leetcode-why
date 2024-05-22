from typing import List


def findMin(nums: List[int]) -> int:
    low, high = 0, len(nums) - 1

    while low < high:
        mid = (low + high) // 2

        if nums[mid] > nums[high]:
            low = mid + 1

        else:
            high = mid

    return nums[low]


print(findMin([4, 5, 6, 7, 0, 1, 2]))
