from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # p, q = list1, list2
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


def create_linked_list(values):
    """ Helper function to create a linked list from a list of values. """
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_linked_list(head):
    """ Helper function to print the linked list. """
    while head:
        print(head.val, end=' -> ' if head.next else '')
        head = head.next
    print()


# Example usage
if __name__ == "__main__":
    # Create a linked list with the binary representation [1,0,1,1]
    ll = create_linked_list([1, 0, 1, 1])
    # print("Linked List: ")
    # print_linked_list(ll)

    # Solve the problem
    solution = Solution()
    result = solution.getDecimalValue(ll)
    print("Decimal Value:", result)
