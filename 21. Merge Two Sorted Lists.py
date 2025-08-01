# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return dummy.next
    
    def makeList(self, list):
        dummy = ListNode()
        curr = dummy
        for val in list:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next
    def printList(self, head):
        while head:
            print(head.val, end="->")
            head = head.next
        print()
sol = Solution()
list1 = sol.makeList([1, 2, 4])
list2 = sol.makeList([1, 3, 4])
merged = sol.mergeTwoLists(list1, list2)
sol.printList(merged)