class Stack():

    def __init__(self, theSize):
        self.top = None
        self.size = theSize
        self.length = 0

    def isFull(self):
        if self.length == self.size:
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.length == 0:
            return True
        else:
            return False
        
    def push(self, data)

class Node():

    def __init__(self, theData):
        self.data = theData
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setNext(self, newNext):
        self.next = newNext
