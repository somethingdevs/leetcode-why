## 150. Evaluate Reverse Polist Notation

### Main idea - Stack

### How did I figure out?

If there is stuff that you need to first go in and come out later, it's a stack problem

### Reasoning

1. Create a stack, could be a list
2. For loop:
    - Its it's an operand (8,9,5), convert to an int and push
    - If it's an operator (-, +, *, /), pop the top two values and solve it according to the operator
      - NOTE - eval() in python is kinda sus, so maybe do something else

3. Return the final value in the stack, voilà!
