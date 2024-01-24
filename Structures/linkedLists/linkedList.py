'''
Implementation of a linked list in python using OOP
'''

class Node(): # a node has data and a pointer to the next node
    
    def __init__(self, theData): # constructor method
        self.data = theData
        self.next = None 
        # linked list is empty when it is initialised so attributes set to none

    def setNext(self, newNext):
        self.next = newNext

    def getNext(self):
        return self.next
    
    def getData(self):
        return self.data

class LinkedList():
    
    def __init__(self):
        self.head = None # Initialise to None as the linked list is empty

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            # update pointers so new node is the head
            newNode.setNext(self.head)
            self.head = newNode

    def traverse(self):
        current = self.head # start at head of list
        
        while current is not None:
            print(current.getData())
            current = current.getNext()

    '''def delete(self, data):
        # start at head of list
        current = self.head
        # check if head node is to be deleted
        if current.getData() == data:
            self.head = current.getNext()
        else:
            while current.getNext != data:
                current = current.getNext
            temp = current.getNext()
            current.setNext(temp.getNext())'''
    ###### commented out method needs work!! PROBLEM ON LINE 52
people = LinkedList()
people.add("Dipsy")
people.add("Po")
people.add("Laa-Laa")
people.traverse()
print(people.head)
print(people) # returns a memory address
people.traverse()
