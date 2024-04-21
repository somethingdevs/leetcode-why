from builtins import ord


def numberOfSpecialChars(word: str) -> int:
    new_word = set(word)
    stack = []
    counter = 0
    for i in sorted(new_word):
        if ord(i) >= 65 and ord(i) <= 90:
            stack.append(i)
        else:
            if i.upper() in stack:
                counter += 1
                stack.remove(i.upper())

    return counter


print(numberOfSpecialChars("BBbab"))
