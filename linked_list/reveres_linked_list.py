class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev



def create_linked_list(elements):
    head = ListNode(elements[0]) if elements else None
    current = head
    for value in elements[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# Example usage
elements = [1, 2, 3, 4, 5]
linked_list = create_linked_list(elements)
print("Original Linked List:")
print_linked_list(linked_list)

reversed_linked_list = reverseList(linked_list)
print("Reversed Linked List:")
print_linked_list(reversed_linked_list)
