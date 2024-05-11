class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # insert code here
        num = 0
        while head:
            num = num * 2 + head.val
            head = head.next

        return num


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
        print(head.val, end=' -> ' if head.next else '\n')
        head = head.next
    print()


if __name__ == "__main__":
    # Create a linked list with the binary representation [1,0,1,1]
    ll = create_linked_list([1, 0, 1])
    print("Linked List: ")
    print_linked_list(ll)

    # Solve the problem
    solution = Solution()
    result = solution.getDecimalValue(ll)
    print("Decimal Value:", result)
