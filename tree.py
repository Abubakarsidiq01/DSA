import collections
# Insert Function
# 1. Define a tree
class Node:
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)

def preorderPrint(r): # root, left, right -> root first(bac)
    if r is None:
        return
    else:
        print(r.data, end="->")
        preorderPrint(r.left)
        preorderPrint(r.right)

def inorderPrint(r): # left, root, right -> ascending order(abc)
    if r is None:
        return
    else:
        inorderPrint(r.left)
        print(r.data, end="->")
        inorderPrint(r.right)
        

def postorderPrint(r): # left, right, root -> last(acb)
    if r is None:
        return
    else:
        postorderPrint(r.left)
        postorderPrint(r.right)
        print(r.data, end="->")
        
#adjacency list
d = {}
def makeList(r):
    if r is None:
        return
    else:
        d[r.data] = []
        if r.left:
            d[r.data].append(r.left.data)
            makeList(r.left)
        if r.right:
            d[r.data].append(r.right.data)
            makeList(r.right)
    return d

def bfs(r):
    queue = collections.deque([r])
    visited =  []
    while queue:
        node = queue.popleft()
        visited.append(node.data)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited
    
def dfs(r):
    stack = [r]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node.data)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited

def search(r, data):
    if r is None:
        return False
    if r.data == data:
        return True
    if data < r.data:
        return search(r.left, data)
    else:
        return search(r.right, data)
"""
def search2(r, key):
    stack = [r]
    visited = []
    while stack:
        node = stack.pop()
        if node.data == key:
            return True
        if node not in visited:
            visited.append(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
    return False
"""

root = Node("g")
root.insert("c")
root.insert("b")
root.insert("a")
root.insert("e")
root.insert("d")
root.insert("f")
root.insert("i")
root.insert("h")
root.insert("j")
root.insert("k")

# Print the tree in order
print("Inorder:")
inorderPrint(root)
print()
print("Preorder:")
preorderPrint(root)
print()
print("Postorder:")
postorderPrint(root)
print()
print("Adjacency List:")
print(makeList(root))
print()
print("BFS:")
print(bfs(root))
print()
print("DFS:")
print(dfs(root))
print()
print("Search:")
print(search(root, "a"))
print(search(root, "b"))
print(search(root, "c"))
print(search(root, "d"))
print(search(root, "e"))
print(search(root, "f"))
print(search(root, "g"))
print(search(root, "h"))
print(search(root, "i"))