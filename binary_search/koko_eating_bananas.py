from typing import List


def minEatingSpeed(piles: List[int], h: int) -> int:
    low, high = 1, max(piles)

    while low <= high:
        mid = (low + high) // 2

        hours_needed = 0
        for pile in piles:
            hours_needed += (pile + mid - 1) // mid

        if hours_needed <= h:
            high = mid - 1
        else:
            low = mid + 1

    return low


piles = [3, 6, 7, 11]
h = 8
print(minEatingSpeed(piles, h))
