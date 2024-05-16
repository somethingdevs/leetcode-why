from utils import ListNode, build_linked_list, print_linked_list
from typing import Optional


class LinkedList:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow, fast = dummy, head

        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return dummy.next


# Example usage
values = [1]
head = build_linked_list(values)
print("Initial linked list:")
print_linked_list(head)

# Create an instance of LinkedList and call removeNthFromEnd
linked_list = LinkedList()
n = 1  # Define n, here it means remove the second node from the end
head = linked_list.removeNthFromEnd(head, n)
print("Linked list after removing the nth node from the end:")
print_linked_list(head)
