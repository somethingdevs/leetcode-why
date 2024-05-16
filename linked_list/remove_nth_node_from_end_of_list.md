## 19. Remove nth node from end of list

### Main reasoning - Two pointers(fast and slow) that follow each other with a difference of n

- Dummy Node: A dummy node is introduced to simplify edge cases, such as when the head needs to be removed. It ensures
  that slow can always start from a node prior to the actual head of the list.
- Advance fast by n Steps: The fast pointer is moved n steps ahead before the main loop begins. This setup ensures the
  correct gap between slow and fast.
- Loop until fast is None: The main loop now runs until fast is None (not fast.next), allowing slow to end up exactly
  before the node that needs to be removed.
- Remove the Node: After the loop, slow.next is adjusted to skip the nth node from the end.