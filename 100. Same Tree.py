# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]
        while stack:
            p, q = stack.pop()
            if p == None and q == None:
                continue
            if p == None or q == None:
                return False
            if p.val != q.val:
                return False

            stack.append((p.left, q.left))
            stack.append((p.right, q.right))
        return True
    def makeTree(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.makeTree(root.left, val)
        else:
            root.right = self.makeTree(root.right, val)
        return root
sol = Solution()
root1 = sol.makeTree(None, 1)
root1 = sol.makeTree(root1, 2)
root1 = sol.makeTree(root1, 3)
root2 = sol.makeTree(None, 1)
root2 = sol.makeTree(root2, 2)
root2 = sol.makeTree(root2, 3)
print(sol.isSameTree(root1, root2))

"""
if p == None and q == None:
    return True
if p == None or q == None:
    return False
if p.val != q.val:
    return False
left = self.isSameTree(p.left, q.left)
roght = self.isSameTree(p.right, q.right)
return left and right
"""