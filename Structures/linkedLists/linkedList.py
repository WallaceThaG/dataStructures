from typing import Any


class Node(): # a node has data and a pointer to the next node
    
    def __init__(self, theData):
        self.data = theData
        self.next = None

    def setNext(self, newNext):
        self.next = newNext

    def getNext(self):
        return self.next
    
    def getData(self):
        return self.data

class LinkedList():
    
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.setNext(self.head)
            self.head = newNode

    def traverse(self):
        current = self.head
        
        while current is not None:
            print(current.getData())
            current = current.getNext()

people = LinkedList()
people.add("Dipsy")
people.add("Po")
people.add("Laa-Laa")
people.traverse()
print(people) # returns a memory address