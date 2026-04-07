from typing import List
from mypy.nodes import defaultdict




# Optimal solution
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = defaultdict(list)
    for word  in strs:
        count = [0] * 26

        for ch in word:
            count[ord(ch) - ord("a")] += 1

        result[tuple(count)].append(word)
    return list(result.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))

# Brute-force solution
# result = {}
# for value in strs:
#     base_word = "".join(sorted(value))
#     if base_word not in result:
#         result[base_word] = []
#     result[base_word].append(value)
#
# return list(result.values())