from utils import ListNode, build_linked_list, print_linked_list
from typing import Optional


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    # Create pointers
    p, q = head, head
    prev = ListNode()

    # Check for only one node
    if not head.next:
        return None

    # Do the do the
    while q and q.next:
        q = q.next.next
        prev = p
        p = p.next

    # Redirect the p-1 to p+1
    if prev:
        prev.next = p.next

    return head


# Example usage
values = [1, 2, 3, 4, 5, 6]
head = build_linked_list(values)
print("Initial linked list:")
print_linked_list(head)

# Delete the middle node
head = delete_middle(head)
print("Linked list after deleting the middle node:")
print_linked_list(head)
