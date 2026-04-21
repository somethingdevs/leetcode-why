from typing import List
from collections import defaultdict


def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = defaultdict(int)

    # Step 1: Build frequency map
    for num in nums:
        freq[num] += 1

    # Step 2: Sort by frequency (descending)
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    # Step 3: Extract top k elements
    result = []
    for i in range(k):
        result.append(sorted_items[i][0])

    return result


nums = [10, 10, 10, 20, 20, 30]
print(topKFrequent(nums=nums, k=2))
