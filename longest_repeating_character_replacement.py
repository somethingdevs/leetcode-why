from collections import defaultdict


# I still don't understand this solution. I might need someone to explain this to me clearly'


def character_replacement(s, k):
    count = defaultdict(int)
    max_freq = max_length = left = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])

        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length


# Example usage
print(character_replacement("AABABBA", 1))
