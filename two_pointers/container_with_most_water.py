from typing import List


def maxArea(height: List[int]) -> int:
    max_area = 0
    left, right = 0, len(height) - 1

    while left < right:
        local_area = (min(height[left], height[right])) * (right - left)
        max_area = max(local_area, max_area)

        if height[left] < height[right]:
            left += 1

        else:
            right -= 1

    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height=height))
