from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hash_map = {}

    for i, n in enumerate(strs):
        temp = ''.join(sorted(n))

        if temp not in hash_map:
            hash_map[temp] = []
        hash_map[temp].append(n)

    return list(hash_map.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
