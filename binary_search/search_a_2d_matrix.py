from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    for i, row in enumerate(matrix):
        low, high = 0, len(matrix[i]) - 1

        # if low < target < high:
        while low <= high:
            mid = (low + high) // 2

            if matrix[i][mid] == target:
                return True

            elif matrix[i][mid] < target:
                low = mid + 1

            else:
                high = mid - 1


    return False

print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
