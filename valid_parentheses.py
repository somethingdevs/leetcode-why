def is_valid(s):
    parentheses_stack = []
    for i in s:

        # If the next character is an opening bracket
        if i in '({[':
            parentheses_stack.append(i)

        # If it's a closing bracket
        else:

            # If it doesn't match, return False
            if not parentheses_stack or \
                    i == ')' and parentheses_stack[-1] != '(' or \
                    i == '}' and parentheses_stack[-1] != '{' or \
                    i == ']' and parentheses_stack[-1] != '[':
                return False
            parentheses_stack.pop()

    # If stack is empty return True
    return not parentheses_stack


print(is_valid('}'))
