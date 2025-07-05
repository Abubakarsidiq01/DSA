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
                if self.data is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.data is None:
                    self.left = Node(data)
                else:
                    self.right.insert(data)

def inorderPrint(r):
    if r is None:
        return
    else:
        inorderPrint(r.left)
        print(r.data, end=" ")
        inorderPrint(r.right)

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
                
    