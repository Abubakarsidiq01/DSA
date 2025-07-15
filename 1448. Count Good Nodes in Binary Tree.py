from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode, use_iterative: bool = False) -> int:
        if use_iterative:
            return self._goodNodesIterative(root)
        else:
            return self._goodNodesRecursive(root)
    
    def _goodNodesRecursive(self, root: TreeNode) -> int:
        def dfs(node, max_so_far):
            if node is None:
                return 0
            left = dfs(node.left, max(node.val, max_so_far))
            right = dfs(node.right, max(node.val, max_so_far))
            ans = left + right
            if node.val >= max_so_far:
                ans += 1
            return ans
        return dfs(root, float("-inf"))
    
    def _goodNodesIterative(self, root: TreeNode) -> int:
        if root is None:
            return 0
        stack = [(root, float("-inf"))]
        ans = 0
        while stack:
            node, max_sf = stack.pop()
            if node.val >= max_sf:
                ans += 1
            if node.left:
                stack.append((node.left, max(node.val, max_sf)))
            if node.right:
                stack.append((node.right, max(node.val, max_sf)))
        return ans

    def makeTree(self, root, val):
        if root is None:
            return TreeNode(val)
        if val < root.val:
            root.left = self.makeTree(root.left, val)
        else:
            root.right = self.makeTree(root.right, val)
        return root

# Test the solution
if __name__ == "__main__":
    sol = Solution()

    # Build this BST: [3, 1, 4, 3, 1, 5]
    root = sol.makeTree(None, 3)
    root = sol.makeTree(root, 1)
    root = sol.makeTree(root, 4)
    root = sol.makeTree(root, 3)
    root = sol.makeTree(root, 1)
    root = sol.makeTree(root, 5)

    print("Recursive DFS Solution:", sol.goodNodes(root, use_iterative=False))
    print("Iterative Solution:", sol.goodNodes(root, use_iterative=True))
"""
if node is None:
    return 0
stack = [(root, float("-inf"))]
ans = 0
while stack:
    node, max_sf = stack.pop()
    if node.val >= max_sf:
        ans += 1
    if node.left:
        stack.append((node.left, max(node.val, max_sf)))
    if node.right:
        stack.append((node.right, max(node.val, max_sf)))
return ans
"""


