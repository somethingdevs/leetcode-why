from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix = [1] * n
    postfix = [1] * n
    result = [1] * n

    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in range(n - 2, -1, -1):
        postfix[i] = postfix[i + 1] * nums[i + 1]

    for i in range(n):
        result[i] = prefix[i] * postfix[i]

    return result


nums = [1, 2, 3, 4]
print(productExceptSelf(nums=nums))
