from typing import List


def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    if len(position) <= 1:
        return 1

    stack = []


print(carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
