from collections import defaultdict


def repeat(sentence):
    sentence = sentence.split(sep=' ')
    max_freq, max_word = 0, ''

    for word in sentence:
        # Temporary defaultdict to count letters for the current word
        letter_freq = defaultdict(int)
        for letter in word:
            letter_freq[letter] += 1

        # Find the maximum frequency of any letter in the current word
        current_max_freq = max(letter_freq.values())
        if current_max_freq > max_freq:
            max_freq = current_max_freq
            max_word = word  # Store the word itself

    print("Word with highest frequency of any letter:", max_word)


repeat('Today is the greatest day ever!')
