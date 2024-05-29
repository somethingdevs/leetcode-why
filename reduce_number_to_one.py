def numSteps(s: str) -> int:
    count = 0
    number = int(s, 2)

    while (number != 1):
        if number % 2 == 0:
            number //= 2
        else:
            number += 1
        count += 1

    return count


print(numSteps("1111011110000011100000110001011011110010111001010111110001"))
