class Node:
    def __init__(self, x: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    # If no values
    if head == None:
        return None

    # First run, creating nodes in between the existing values
    current = head
    while current:
        new_node = Node(current.val)
        new_node.next = current.next
        current.next = new_node
        current = new_node.next

    # Second run, assigning randoms of the nodes
    current = head
    while current:
        if current.random:
            current.next.random = current.random.next
        else:
            current.next.random = None
        current = current.next.next

    # Third run, seperating the old and new connections
    current = head
    new_head = head.next
    new_current = new_head
    while current:
        current.next = new_current.next
        current = current.next
        if current:
            new_current.next = current.next
        new_current = new_current.next

    return new_head


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
