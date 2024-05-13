from utils import ListNode, build_linked_list, print_linked_list
from typing import Optional


class LinkedList:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # First only has one value
        first = ListNode(next=head)

        # Everything will be done with p
        p = first

        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next

        return first.next


# Example usage
values = [1, 2, 6, 3, 4, 5, 6]
head = build_linked_list(values)
print("Initial linked list:")
print_linked_list(head)

# Create an instance of LinkedList and call removeElements
linked_list = LinkedList()
head = linked_list.removeElements(head, 6)
print("Linked list after removing elements:")
print_linked_list(head)
