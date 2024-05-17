from utils import ListNode, build_linked_list, print_linked_list
from typing import List, Optional


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

        # Attach the remaining elements
        current.next = list1 if list1 else list2

        return dummy.next

    # not entirely sure whats happening
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_list = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                merged_list.append(merged_list(l1, l2))
            lists = merged_list

        return lists[0]


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
