from functools import reduce
from operator import mul
from typing import List
from collections import defaultdict


def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    count = 0
    window = []
    product = 1

    if k <= 1:
        return 0

    for num in nums:
        window.append(num)
        product *= num

        while product >= k and window:
            product //= window.pop(0)

        count += len(window)

    return count


print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
print(numSubarrayProductLessThanK([1, 2, 3], 0))
