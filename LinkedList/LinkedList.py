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

    def traverse(self):
        # we want to iterate all the nodes for the list.
        # extracting all the nodes form the list
        char=self.head
        while char is not None:
            print(char.data)
            char=char.next

    def __str__(self):
        char = self.head
        result=""
        while char is not None:
            result+=str(char.data)+'->'
            char = char.next
        return result[:-2]


    # adding form tail
    def tail(self,value):
        new_node=Node(value) # creating new node using new value
        if self.head is None: # Checking if linkedlist is none or not
            self.head=new_node # if yes updating new node with head
            self.n+=1 # updating count of the n
            return
        char=self.head        #retrieving first node stored as in head to connect retrieve others
        while char.next!=None: # reaching till next is storing address of the next node
            char=char.next     # updating char with next add to check what to check None
        char.next=new_node     # after the while we get the last node with None at its next and updating its tail with new created to append
        self.n+=1              #updating n to maintain correct cont of the node for the linkedlist



    def Insert_after_value (self,after, value):
        # we need reach to value and its node
        new_node=Node(value)

        char=self.head

        while char is  not None:
            if char.data==after:
                break
            char = char.next

        if char is not None: #after breaking if condition char is not None
            new_node.next=char.next
            char.next=new_node
        else: #after while loop execute
             return "Item not fount"





L=LinkedList()
# L.insert_head(12)
# L.insert_head(13)
# L.insert_head(14)
# L.insert_head("Bhinge")
# L.insert_head(16)
# L.insert_head(1)
# L.insert_head(3)
# L.insert_head(4)
# L.insert_head(5)
# L.insert_head(6)
# L.insert_head("vaibhav")
print("LinkedList: ",L)
print("Length of linkedList: ",len(L))
L.traverse()
print("Printing linkedlist: ", L)
L.tail(10)
L.Insert_after_value(11,12)
print("adding tail: ",L)