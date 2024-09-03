from utils import ListNode, build_linked_list, print_linked_list
from typing import List, Optional


class Solution:

    # Helper function to merge two lists
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
        else:
            current.next = list2

        return dummy.next

    # not entirely sure whats happening
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_lists.append(self.mergeTwoLists(l1, l2))

            lists = merged_lists

        return lists[0] if lists else None


# Example usage
if __name__ == "__main__":
    sol = Solution()

    # Creating lists
    list_nodes = [
        build_linked_list([1, 4, 5]),
        build_linked_list([1, 3, 4]),
        build_linked_list([2, 6])
    ]

    # Merging k lists
    merged_head = sol.mergeKLists(list_nodes)
    print("Merged List:")
    print_linked_list(merged_head)
