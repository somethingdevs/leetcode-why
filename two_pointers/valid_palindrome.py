def isPalindrome(s: str) -> bool:
    new_string = ''

    for i in s:
        if i.isalpha() or i.isnumeric():
            new_string += i.lower()

    left, right = 0, len(new_string) - 1
    while left < right:
        if new_string[left] != new_string[right]:
            return False

        left += 1
        right -= 1
    return True


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))
