# Definition for singly-linked list.
from typing import Optional
class ListNode:
     def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

        #If the list is cycle, the fast pointer will definitely catch up with the slow pointer

n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(-4)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n2  

sol = Solution()
print(sol.hasCycle(n1))  


"""
        ans = set()
        while head:
            if head in ans:
                return True
            ans.add(head)
            head = head.next
        return False


I used set because:
You're not storing the value of the node you're storing the node object itself in memory. Each Node (or ListNode) is treated as a unique object, even if two nodes have the same value.
n1 = Node(10)
n2 = Node(10)
print(n1 == n2)        # False → different objects
print(n1.value == n2.value)  # True → same value
"""

        