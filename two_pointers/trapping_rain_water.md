## 42. Trapping Rain Water

### Main idea - Creating lists and expression min(max_left, max_right) - height

### Reasoning

1. Need to make two lists; max_left and max_right.
2. max_left is created by checking what was the maximum from the left side so far.
3. max_right is created by checking what was the maximum from the right side so far. Basically the reverse.
4. Run a loop and calculate the following
    1. water += min(max_left, max_right) - height

Basically if the value is lower than 0, then ignore it, or else run with it.
