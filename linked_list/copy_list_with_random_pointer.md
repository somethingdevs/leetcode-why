## 138. Copy List with Random Pointer

### Main idea - Hashmap to store Nodes

#### Reasoning

1. Initialize a hashamp with a key value both None
2. This requires two passes
3. First pass, you make nodes with the values while going through the list. The nodes you assign them to the hash map.
4. Second pass, you assign all the next and random pointers.
5. Return the hashmap[head]