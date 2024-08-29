def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left, max_length = 0, 0

    for i, n in enumerate(s):

        while n in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(n)
        max_length = max(max_length, i - left + 1)

    return max_length


s = "pwwkew"
print(lengthOfLongestSubstring(s))
