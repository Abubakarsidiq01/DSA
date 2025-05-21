from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
            
        slow = head
        fast = slow.next

        while slow and fast:
            if slow.val == fast.val:
                slow.next = fast.next
            else:
                slow = fast
            fast = slow.next
        return head

def print_from_node(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None") 
    

n1 = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(2)
n4 = ListNode(3)
n5 = ListNode(3)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5  

sol = Solution()
middle = sol.deleteDuplicates(n1)
print_from_node(middle)        