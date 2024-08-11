#linked list  are linear data structures where the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers

#creating a linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
node4 = Node(4)

#linking the nodes
Node1.next = Node2
Node2.next = Node3
Node3.next = node4

#accessing the data of Node1
print(Node1.data)




