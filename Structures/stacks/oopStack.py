class Stack():

    # constructor
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)

        # check if stack is not empty
        if not self.isEmpty():
            # point to next element in the list
            newNode.setNext(self.top)
        # set top to the new node
        self.top = newNode

    def pop(self):
        poppedData = None
        # check if empty
        if self.isEmpty():
            print("ERR: STACK UNDERFLOW")
        else:
            poppedData = self.top.getData()
            self.top = self.top.getNext()

        return poppedData

    def peek(self):
        peekedData = None

        if self.isEmpty():
            print("ERR: STACK EMPTY")
        else:
            peekedData = self.top.getData()

        return peekedData
    
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
        

class Node():

    # constructor
    def __init__(self, theData):
        self.data = theData
        self.next = None

    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setNext(self, newNext):
        self.next = newNext

def useStack():
    myStack = Stack()
    print(myStack.peek())
    myStack.push("Beans")
    myStack.push("Greens")
    myStack.push("Potatos")
    myStack.push("Tomatos")
    myStack.push("Yams")
    myStack.push("Hams")

    peekedItem = myStack.peek()
    print(peekedItem)

    for i in range(8):
        poppedItem = myStack.pop()
        print(poppedItem)

useStack()