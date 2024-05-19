# TODO: Do this problem!
def daily_temperatures(temps):
    result = [0] * len(temps)
    stack = []

    for i, temp in enumerate(temps):
        while stack and temps[stack[-1]] < temp:
            index = stack.pop()
            result[index] = i - index
        stack.append(i)

    return result


print(daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]))
