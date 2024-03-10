def eval_rpn(tokens):
    comp_stack = []
    op = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: int(x / y),
    }

    for char in tokens:
        if char not in op:
            comp_stack.append(int(char))

        else:
            val2 = comp_stack.pop()
            val1 = comp_stack.pop()
            expression = int(eval(f'{val1} {char} {val2}'))
            comp_stack.append(expression)
    return comp_stack[0]


print(eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
