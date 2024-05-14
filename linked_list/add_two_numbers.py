from utils import ListNode, build_linked_list, print_linked_list
from typing import Optional


class LinkedList:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize everything
        first, second = l1, l2
        dummy = ListNode(0)
        result = dummy
        carry = 0

        # Loop until both lists are exhausted and no carry remains
        while first or second or carry:
            val1 = first.val if first else 0
            val2 = second.val if second else 0

            # Sum the values and the carry
            total = val1 + val2 + carry
            carry = total // 10  # Get new carry

            # Create a new node with the sum mod 10
            result.next = ListNode(total % 10)
            result = result.next

            # Move pointers if possible
            if first:
                first = first.next
            if second:
                second = second.next

        return dummy.next


# Example usage
values1 = [2, 4, 3]  # Represents the number 342
values2 = [5, 6, 4]  # Represents the number 465

l1 = build_linked_list(values1)
l2 = build_linked_list(values2)

print("First Number (as linked list):")
print_linked_list(l1)

print("Second Number (as linked list):")
print_linked_list(l2)

# Create an instance of LinkedList and call addTwoNumbers
linked_list = LinkedList()
result = linked_list.addTwoNumbers(l1, l2)

print("Resultant Sum (as linked list):")
print_linked_list(result)
