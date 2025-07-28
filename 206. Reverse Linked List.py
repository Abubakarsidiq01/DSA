from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = head
        while curr:
            next = curr.next
            curr.next = dummy.next
            dummy.next = curr
            curr = next
        return dummy.next

    def printList(self, head: Optional[ListNode]) -> None:
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

    def buildList(self, values):
        dummy = ListNode()
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

# Test it
s = Solution()
linked_list = s.buildList([1, 2, 3, 4, 5])
reversed_list = s.reverseList(linked_list)
s.printList(reversed_list)
