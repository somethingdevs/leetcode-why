from utils import ListNode, build_linked_list, print_linked_list
from typing import Optional


class LinkedList:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pass


# Example usage
values = [1, 2, 3, 4, 5]
head = build_linked_list(values)
print("Initial linked list:")
print_linked_list(head)

# Create an instance of LinkedList and call reorderList
linked_list = LinkedList()
linked_list.reorderList(head)
print("Linked list after reordering:")
print_linked_list(head)
