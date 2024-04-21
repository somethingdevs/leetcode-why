from collections import defaultdict


def numberOfSpecialChars(word: str) -> int:
    first_uppercase = {}
    last_lowercase = {}

    # Record the first and last positions for each character
    for index, char in enumerate(word):
        if char.islower():
            if char not in last_lowercase:
                last_lowercase[char] = index
            last_lowercase[char] = index
        else:
            char_lower = char.lower()
            if char_lower not in first_uppercase:
                first_uppercase[char_lower] = index

    # Count special characters
    special_count = 0
    for char in last_lowercase:
        if char in first_uppercase:
            if last_lowercase[char] < first_uppercase[char]:
                special_count += 1

    return special_count


print(numberOfSpecialChars('aaAbcBC'))
