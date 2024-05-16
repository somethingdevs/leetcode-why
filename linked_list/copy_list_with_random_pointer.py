class Node:
    def __init__(self, x: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    old_hash_map = {None: None}

    # First pass where you just create copy of the node and set the node to the hash map
    current = head
    while current:
        copy = Node(current.val)
        old_hash_map[current] = copy
        current = current.next

    # Second pass where you take those copies of the nodes in the hashmap and point them correctly
    current = head
    while current:
        copy = old_hash_map[current]
        copy.next = old_hash_map[current.next]
        copy.random = old_hash_map[current.random]
        current = current.next

    return old_hash_map[head]


def print_list(node: 'Optional[Node]'):
    while node:
        random_val = node.random.val if node.random else 'None'
        print(f'Node val: {node.val} with random pointing to: {random_val}')
        node = node.next


# Create nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Link nodes
node1.next = node2
node2.next = node3

# Add random pointers
node1.random = node3
node2.random = node1
node3.random = None

# Test copyRandomList function
copied_list_head = copyRandomList(node1)

# Print original and copied list to verify the copy
print("Original list:")
print_list(node1)
print("Copied list:")
print_list(copied_list_head)
