from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head
        while current:
            count += 1
            current = current.next
        ans = count // 2

        current = head
        for i in range(ans):
            current = current.next
        return current
"""
Once you return current, you are returning the node object at the middle.That node
still points to the rest of the list! So printing from that node will print to the end.
"""
   
#So the code can be printed and seen
def print_from_node(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None") 
    

n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(0)
n4 = ListNode(1)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5  

sol = Solution()
middle = sol.middleNode(n1)
print_from_node(middle)
          