from utils import ListNode, build_linked_list, print_linked_list
from typing import Optional


def middleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    # Create nodes
    p, q = head, head

    # Base case for only 1 pointer
    if not head.next:
        return head

    # Normal logic
    while q and q.next:
        p = p.next
        q = q.next.next

    return p


# Example usage
values = [1, 2, 3, 4, 5]
head = build_linked_list(values)
print("Initial linked list:")
print_linked_list(head)

# Find the middle node
middle = middleNode(head)
if middle:
    print(f"The middle node value is: {middle.val}")
else:
    print("The middle node could not be determined.")
