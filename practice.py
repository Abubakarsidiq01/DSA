class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Sll:
    def __init__(self):
        self.head = None
        
    def traversal(self):
        a = self.head
        while a is not None:
            print(a.val, end="-->")
            a = a.next
            
    def insert_at_beginning(self, val):
        print()
        nb = Node(val)
        nb.next = self.head
        self.head = nb
        
    def insert_at_end(self, val):
        print()
        ne = Node(val)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne
        
    def insert_at_position(self, val, pos):
        print()
        np = Node(val)
        a = self.head
        for i in range(1, pos-1):
            a = a.next
        np.next = a.next
        a.next = np
        
    
            
        
            
n1 = Node(5)
sll = Sll()
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3
n4 = Node(20)
n3.next = n4
sll.traversal()

sll.insert_at_beginning(2) #calling the insert at the beginning
sll.traversal()  # to print it together with the rest    

sll.insert_at_end(25) #calling the insert at the end
sll.traversal ()

sll.insert_at_position(12, 3)
sll.traversal()
