def lengthOfLastWord(s: str) -> int:

    return s.strip().split(sep=' ')[-1]


print(lengthOfLastWord(s="luffy is still joyboy"))
