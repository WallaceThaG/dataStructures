class Node():
    def __init__(self, theData):
        self.data = theData
        self.next = None

class LinkedList():
    def __init__(self, theHeadData):
        self.head = Node(theHeadData)

people = LinkedList("Zhandos")
print(people) # returns a memory address
print(people.head.data)
print(people.head.next) # returns none because there is only one element in the linked lilstpyt