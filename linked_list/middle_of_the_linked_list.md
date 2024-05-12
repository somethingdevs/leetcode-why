## 876. Middle of the Linked List

### Main idea - Linked List + Two pointers

#### Reasoning

1. Very simple. Use a slow pointer that moves at normal traversal speed. Use another pointer that moves at 2x traversal
   speed.
2. Ofc you also need to check the case where you only have one item in the list. 