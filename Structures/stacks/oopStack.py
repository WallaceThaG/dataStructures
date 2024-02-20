class Stack():

    def __init__(self):
        self.top = None

    def pop(self):
        
        
class Node():

    def __init__(self, theData, thePrev):
        self.data = theData
        self.previous = thePrev

    def push(self, newNext):
        self.top = newNext
        