def cal_points(operations):
    stack = []
    for op in operations:
        if op == 'C':
            stack.pop()

        elif op == 'D':
            stack.append(2 * stack[-1])

        elif op == '+':
            stack.append(stack[-1] + stack[-2])

        else:
            stack.append(int(op))

    return sum(stack)


print(cal_points(["5", "-2", "4", "C", "D", "9", "+", "+"]))
