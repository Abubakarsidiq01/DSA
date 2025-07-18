# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left or right
    """
    the last return sentence is the same as this    
    if left:
        return left
    return right
    """
    def makeTree(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.makeTree(root.left, val)
        else:
            root.right = self.makeTree(root.right, val)
        return root

# Test code
sol = Solution()
root = sol.makeTree(None, 3)
root = sol.makeTree(root, 5)
root = sol.makeTree(root, 1)
root = sol.makeTree(root, 6)
root = sol.makeTree(root, 2)
root = sol.makeTree(root, 0)
root = sol.makeTree(root, 8)
root = sol.makeTree(root, 7)
root = sol.makeTree(root, 4)

# The tree structure is:
#       3
#      / \
#     1   5
#    / \ / \
#   0  2 4  6
#         / \
#        7   8

# Test cases using actual nodes from the tree
print("Tree structure:")
print("       3")
print("      / \\")
print("     1   5")
print("    / \\ / \\")
print("   0  2 4  6")
print("         / \\")
print("        7   8")
print()

# Test 1: LCA of 1 and 5 should be 3
print(f"LCA of 1 and 5: {sol.lowestCommonAncestor(root, root.left, root.right).val}")

# Test 2: LCA of 1 and 2 should be 1
print(f"LCA of 1 and 2: {sol.lowestCommonAncestor(root, root.left, root.left.right).val}")

# Test 3: LCA of 0 and 2 should be 1
print(f"LCA of 0 and 2: {sol.lowestCommonAncestor(root, root.left.left, root.left.right).val}")

# Test 4: LCA of 4 and 6 should be 5
print(f"LCA of 4 and 6: {sol.lowestCommonAncestor(root, root.right.left, root.right.right).val}")

# Test 5: LCA of 7 and 8 should be 6
print(f"LCA of 7 and 8: {sol.lowestCommonAncestor(root, root.right.right.left, root.right.right.right).val}")

# Test 6: LCA of 0 and 8 should be 3 (root)
print(f"LCA of 0 and 8: {sol.lowestCommonAncestor(root, root.left.left, root.right.right.right).val}")