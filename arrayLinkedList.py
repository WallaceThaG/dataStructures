linkedList = [
    ["Bob", 3],
    ["Sarah", 2],
    ["Shanon", None],
    ["Roberto", 1],
    [None,None],
    [None,None]
]

head = 0 # head pointer points to the first item in the linked list

def traverse():
    
    current = head # set current pointer to the head pointer

    while current != None: # iterates until the end of the linked list (indicated by a null value)
        print(linkedList[current][0])
        current = linkedList[current][1] # update current pointer

def addItem(item):

    current = head
    empty = getEmpty()

    while current != None:
        if linkedList[current][1] == None:
            print(empty)
            linkedList[empty][0] = item
            print(linkedList[empty][0], linkedList[empty][1])
            linkedList[current][1] = empty
        current = linkedList[current][1]
        
def getEmpty():

    for i in range(0, len(linkedList)):
        if linkedList[i][0] == None:
            return i


traverse()
addItem("Zhandos")
traverse()