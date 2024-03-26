from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        list_length = 0
        while current:
            print(current.val)
            list_length += 1
            current = current.next
        print(list_length)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(1)

# Check if the linked list is a palindrome
solution = Solution()
print(solution.isPalindrome(head))
