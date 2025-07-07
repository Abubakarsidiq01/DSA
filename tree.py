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

def inorderPrint(r): # left, root, right -> ascending order(abc)
    if r is None:
        return
    else:
        inorderPrint(r.left)
        print(r.data, end="->")
        inorderPrint(r.right)
        
def preorderPrint(r): # root, left, right -> root first(bac)
    if r is None:
        return
    else:
        print(r.data, end="->")
        preorderPrint(r.left)
        preorderPrint(r.right)

def postorderPrint(r): # left, right, root -> last(acb)
    if r is None:
        return
    else:
        postorderPrint(r.left)
        postorderPrint(r.right)
        print(r.data, end="->")
        

root = Node("g")
root.insert("c")
root.insert("b")
root.insert("a")
root.insert("e")
root.insert("d")
root.insert("f")
root.insert("h")
root.insert("i")
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
    