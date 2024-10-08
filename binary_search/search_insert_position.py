from typing import List


def searchInsert(nums: List[int], target: int) -> int:
    left, right, mid = 0, len(nums) - 1, 0

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return left


nums = [1, 3, 5, 6]
target = 5
print(searchInsert(nums=nums, target=target))
