# I still don't understand this solution. I might need someone to explain this to me clearly'


def character_replacement(s, k):
    max_length = 0

    for target_char in range(26):  # Iterate over all possible characters 'A' to 'Z'
        left = 0
        count = 0

        for right in range(len(s)):
            if ord(s[right]) - ord('A') == target_char:
                count += 1

            while (right - left + 1) - count > k:
                if ord(s[left]) - ord('A') == target_char:
                    count -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

    return max_length


# Example usage
print(character_replacement("AABABBA", 1))
