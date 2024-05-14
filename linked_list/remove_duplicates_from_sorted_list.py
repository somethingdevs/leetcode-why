from utils import ListNode, build_linked_list, print_linked_list
from typing import Optional


class LinkedList:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        current = head

        while current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head


# Example usage
values = [1, 1, 2, 3, 3]
head = build_linked_list(values)
print("Initial linked list:")
print_linked_list(head)

# Create an instance of LinkedList and call delete_duplicates
linked_list = LinkedList()
head = linked_list.delete_duplicates(head)
print("Linked list after removing duplicates:")
print_linked_list(head)
