from utils import ListNode, build_linked_list, print_linked_list
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1

        elif list2:
            current.next = list2

        return dummy.next

# Example usage
values1 = [1, 2, 4]
values2 = [1, 3, 4]

l1 = build_linked_list(values1)
l2 = build_linked_list(values2)

print("First Linked List:")
print_linked_list(l1)

print("Second Linked List:")
print_linked_list(l2)

# Create an instance of Solution and call mergeTwoLists
solution = Solution()
result = solution.mergeTwoLists(l1, l2)

print("Merged Linked List:")
print_linked_list(result)
