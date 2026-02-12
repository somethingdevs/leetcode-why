# Approach 1
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}

    for index, value in enumerate(s):
        count_s[value] = 1 + count_s.get(value, 0)
        count_t[t[index]] = 1 + count_t.get(t[index], 0)

    for c in count_s:
        if count_s[c] != count_t.get(c, 0):
            return False

    return True


# Approach 2
def isAnagram(s: str, t: str) -> bool:
    s = sorted(s)
    t = sorted(t)

    if s != t:
        return False
    return True

s = "anagram"
t = "nagaram"
print(isAnagram(s, t))