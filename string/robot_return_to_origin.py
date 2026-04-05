def judgeCircle(moves: str) -> bool:
    position = (0,0)
    for index, value in enumerate(moves):
        print(value, index)

        if value == 'U':
            position = (position[0], position[1] + 1)
        elif value == 'D':
            position = (position[0], position[1] - 1)
        elif value == 'L':
            position = (position[0] - 1, position[1])
        elif value == 'R':
            position = (position[0] + 1, position[1])

    if position == (0,0):
        return True
    else:
        return False

moves = "LL"
output = judgeCircle(moves)

print(output)