from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


def build_linked_list(values):
    """ Builds a linked list from a list of values and returns the head of the list. """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_linked_list(head: Optional[ListNode]):
    """ Prints the linked list from the head to the end. """
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


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
