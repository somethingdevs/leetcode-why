## 22. Generate Parenthesis

## Main idea - Backtracking + Stack

## How did I figure it out?

I did not. I still don't understand wtf is going on, but I think kinda like, if you gonna do something in which there's
a
lot of checking all possible conditions, then you backtrack.

### Reasoning

1. Only add open parenthesis if open < n
2. Only add a closing parenthesis if closed < open
3. Valid IFF open == closed == n