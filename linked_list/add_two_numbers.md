## 2. Add two numbers

### Main idea - Linked List traversal with some variables

### Process Breakdown:

1. **Initialization**: You're right about using two pointers, `first` and `second`, for iterating through the two linked
   lists. You also correctly identified the need for a `carry` variable, which will indeed hold values of either 0 or 1,
   depending on whether the sum of the values in the current nodes and any carry from the previous nodes exceeds 9.

2. **Iteration**: Your idea to use a while loop that continues until both `first` and `second` are `None` is good.
   However, you should consider that one list might be longer than the other. Thus, the condition should
   be `while first is not None or second is not None or carry != 0`. The carry needs to be checked in case there’s a
   carry after the last elements of the lists have been processed (e.g., adding `999` and `1`).

3. **Summing Nodes**: For each step of the loop, you should:
    - Add the values of `first` and `second` if they are not `None`. If either is `None`, treat its value as 0.
    - Add the carry from the previous iteration.
    - Compute the new digit as `(value1 + value2 + carry) % 10`.
    - Update the carry as `(value1 + value2 + carry) // 10`.

4. **Result Linked List**: Use a dummy head node for the result linked list. This simplifies node insertion as you can
   keep appending new nodes to it without losing the reference to the head of the result list. Update a tail pointer to
   keep track of the last node.

5. **End of Process**: Check after the loop if there is any carry left and add a new node if there is.