## 203. Remove Linked List Elements

### Main idea - Linked List pointer traversal

#### Reasoning

1. Basically use a pointer to scroll through the linked list.
2. If the next value is the value that needs to be deleted then re-adjust the pointers in such a way that you skip (or
   delete it)
3. Else just continue moving along normally
4. Return the head. (keep a dummy pointer, pointing to the head)