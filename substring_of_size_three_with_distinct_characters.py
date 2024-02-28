def count_good_substring(s):
    good_window = {}
    counter = 0

    if len(s) < 3:
        return 0

    # Initialize the values of the first three elements of the window
    for i in range(0, 3):
        good_window[s[i]] = good_window.get(s[i], 0) + 1

    if len(good_window.keys()) == 3:
        counter += 1

    for i in range(3, len(s)):


        good_window[s[i]] = good_window.get(s[i], 0) + 1
        good_window[s[i - 3]] = good_window.get(s[i - 3], 0) - 1

        if good_window[s[i - 3]] == 0:
            del good_window[s[i - 3]]

        if len(good_window.keys()) == 3:
            counter += 1


    return counter


# Important Quality about sets is that it does not allow for duplicates

print(count_good_substring('aababcabc'))
