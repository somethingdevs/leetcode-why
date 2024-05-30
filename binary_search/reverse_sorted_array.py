def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + ((right - left) // 2)

        if target == nums[mid]:
            return mid

        elif target < nums[mid]:
            left = mid + 1

        else:
            right = mid - 1

    return -1


print(search([20, 17, 15, 14, 14, 13, 12, 10, 9, 8, 4], 4))
