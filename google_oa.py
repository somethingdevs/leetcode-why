def first_question(digits):
    largest_number = 0
    n = len(digits)

    for i in range(n):
        largest_number = max(largest_number, digits[i])

        for j in range(i + 1, n):
            second_digit = digits[i] * 10 + digits[j]
            largest_number = max(largest_number, second_digit)

            for k in range(j + 1, n):
                third_number = digits[i] * 100 + digits[j] * 10 + digits[k]
                largest_number = max(largest_number, third_number)

    return largest_number


def second_question(arr):
    moves = arr[0]

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            moves += arr[i] - arr[i - 1]

    return moves


digits = [7, 2, 3, 3, 4, 9]
arr = [2, 2, 0, 0, 1]
print(first_question(digits))
print(second_question(arr))
