class Node:
    def __init__(self,value):
        #node store data value in head
        self.data=value
        #last node is last is  None
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None
        self.n=0

    def __len__(self):
        return self.n

    def insert_head(self,value):
        #new node
        new_node=Node(value)
        #create connection
        new_node.next=self.head
        #reassign
        self.head=new_node
        #increment
        self.n=self.n+1

L=LinkedList()
L.insert_head(12)
L.insert_head(13)
L.insert_head(14)
L.insert_head(15)
L.insert_head(16)
L.insert_head("vaibhav")
# print("LinkedList: ",L)

print("Length of linkedList: ",len(L))
