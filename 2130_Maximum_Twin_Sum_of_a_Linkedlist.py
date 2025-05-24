from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head is None or head.next is None:
            return head

        lst = []
        b = -1 #poimter at the end of the list
        c = 0 #pointer atthe beggining of the list
        ans = 0
        # converting the linked list in to a list
        while head:
            lst.append(head.val)
            head = head.next
    
        for i in range(len(lst)//2):
            ans = max(ans, lst[c] + lst[b])
            b -= 1
            c += 1
        return ans

    
n1 = ListNode(5)
n2 = ListNode(2) 
n3 = ListNode(3)
n4 = ListNode(4) 

n1.next = n2
n2.next = n3
n3.next = n4

sol = Solution()
result = sol.pairSum(n1)
print(result)




