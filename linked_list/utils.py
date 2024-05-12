from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values):
    """Builds a linked list from a list of values and returns the head of the list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_linked_list(head: Optional[ListNode]):
    """Prints the linked list from the head to the end."""
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
