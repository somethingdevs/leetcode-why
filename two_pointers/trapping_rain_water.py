from typing import List


def trap(height: List[int]) -> int:
    total_water = 0
    max_left, max_right = [], [0] * len(height)
    current_left, current_right = 0, 0

    # Fill max_left
    for i, val in enumerate(height):
        max_left.append(current_left)
        if current_left < val:
            current_left = val

    # Fill max_right
    for i in range(len(height) - 1, -1, -1):
        max_right[i] = current_right
        if current_right < height[i]:
            current_right = height[i]


    for i, val in enumerate(height):
        exp = min(max_left[i], max_right[i]) - height[i]
        if exp >= 0:
            total_water += exp

    return total_water


print(trap([4,2,0,3,2,5]))
