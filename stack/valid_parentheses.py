def is_valid(s):
    stack = []
    paranthesis_mapping = {')': '(', ']': '[', '}': '{'}

    for bracket in s:
        if bracket in paranthesis_mapping.values():
            stack.append(bracket)
        else:
            if not stack or stack[-1] != paranthesis_mapping[bracket]:
                return False
            stack.pop()

    return not stack


print(is_valid('()[]{}'))
