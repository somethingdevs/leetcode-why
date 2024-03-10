def generate_parenthesis(n):
    """Returns all possible parenthesis permutations"""
    stack = []
    res = []

    def backtrack(open, closed):
        """"Does the backtracking"""

        if open == closed == n:
            res.append(''.join(stack))
            return

        if open < n:
            stack.append('(')
            backtrack(open + 1, closed)
            stack.pop()

        if closed < open:
            stack.append(')')
            backtrack(open, closed + 1)
            stack.pop()

    backtrack(0, 0)
    return res


print(generate_parenthesis(3))
