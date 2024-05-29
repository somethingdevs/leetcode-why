from typing import List


def findLucky(arr: List[int]) -> int:
    result = -1

    for i in arr:
        if arr.count(i) == i:
            result = max(result, i)

    return result


print(findLucky([1, 2, 2, 3, 3, 3]))
