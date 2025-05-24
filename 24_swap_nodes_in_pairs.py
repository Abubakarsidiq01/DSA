from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        curr = head.next # a dummy so we can reference and print latter
        prev = None

        while head and head.next:
            if prev:
                prev.next = head.next
            prev = head
            nextNode = head.next.next
            head.next.next = head

            head.next = nextNode
            head = nextNode
        return curr 


def print_from_node(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# Test cases
# Test case 1: Even number of nodes
n1 = ListNode(1)
n2 = ListNode(2) 
n3 = ListNode(3)
n4 = ListNode(4)

n1.next = n2
n2.next = n3
n3.next = n4

print("Original list:")
print_from_node(n1)

sol = Solution()
result = sol.swapPairs(n1)

print("After swapping pairs:")
print_from_node(result)

# Test case 2: Odd number of nodes
n5 = ListNode(1)
n6 = ListNode(2)
n7 = ListNode(3)

n5.next = n6
n6.next = n7

print("\nOriginal list:")
print_from_node(n5)

result2 = sol.swapPairs(n5)

print("After swapping pairs:")
print_from_node(result2)

# Test case 3: Single node
n8 = ListNode(1)

print("\nOriginal list:")
print_from_node(n8)

result3 = sol.swapPairs(n8)

print("After swapping pairs:")
print_from_node(result3)

# Test case 4: Empty list
result4 = sol.swapPairs(None)

print("\nEmpty list after swapping:")
print_from_node(result4)
