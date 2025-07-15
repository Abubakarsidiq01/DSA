from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        stack = [(root, 0)] 

        while stack:
            node, curr = stack.pop()
            if node.left == None and node.right == None:
                if (node.val + curr) == targetSum:
                    return True
            curr += node.val
            if node.left:
                stack.append((node.left, curr))
            if node.right:
                stack.append((node.right, curr))
        return False
    
    def makeTree(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.makeTree(root.left, val)
        else:
            root.right = self.makeTree(root.right, val)
        return root
    
sol = Solution()
root = sol.makeTree(None, 5)
root = sol.makeTree(root, 4)
root = sol.makeTree(root, 8)
root = sol.makeTree(root, 11)
root = sol.makeTree(root, 13)
root = sol.makeTree(root, 4)
root = sol.makeTree(root, 7)
print(sol.hasPathSum(root, 22))
print(sol.hasPathSum(root, 23))
