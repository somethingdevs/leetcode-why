"""
This module defines a function contains_nearby_duplicate that checks for the presence
 of any duplicate numbers within 'k' distance from each other in a list.
"""


def contains_nearby_duplicate(nums, k):
    duplicate_window = set()

    # Basically we keep running the loop until we reach the end
    for i in range(len(nums)):

        # Checking if the number in the nums list is in the duplicate_window set or not.
        # When the duplicate is caught, even if it's in the same window, then it returns True
        if nums[i] in duplicate_window:
            return True

        # Add nums[i] to the duplicate_window
        duplicate_window.add(nums[i])

        if len(duplicate_window) > k:
            duplicate_window.remove(nums[i - k])

    return False


print(contains_nearby_duplicate([1, 2, 3, 1, 2, 3], 4))
