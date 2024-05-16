from utils import ListNode, build_linked_list, print_linked_list
from typing import Optional


class LinkedList:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        # Keep iterating and praying that they come to each other
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Helper function to create a cycle in the list
def insert_cycle(head: ListNode, pos: int) -> ListNode:
    if pos == -1:
        return head
    cycle_entry = None
    current = head
    index = 0
    while current.next:
        if index == pos:
            cycle_entry = current
        current = current.next
        index += 1
    current.next = cycle_entry  # Create a cycle by pointing the last node to the cycle_entry
    return head


# Example usage
values = [3, 2, 0, -4]
head = build_linked_list(values)
head = insert_cycle(head, 1)  # Creates a cycle where the last node points back to the second node

# Create an instance of LinkedList and check for cycle
linked_list = LinkedList()
if linked_list.hasCycle(head):
    print("Cycle detected in the list.")
else:
    print("No cycle detected in the list.")
