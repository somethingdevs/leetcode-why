def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    result = [-1] * len(nums1)
    next_greater_list = {}
    stack = []

    for num in reversed(nums2):
        while stack and stack[-1] <= num:
            stack.pop()

        if stack:
            next_greater_list[num] = stack[-1]
        stack.append(num)

    for index, num in enumerate(nums1):
        if num in next_greater_list:
            result[index] = next_greater_list[num]

    return result


print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))
