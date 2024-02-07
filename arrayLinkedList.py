linkedList = [
    ["Bob", 3],
    ["Sarah", 2],
    ["Shanon", 4],
    ["Roberto", 1],
    ["Gromit", 5],
    ["Wallace",None]
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

    if empty == None:
        print("ERR: LIST FULL")
    else:
        while current != None:
            if linkedList[current][1] == None:
                linkedList[empty][0] = item
                linkedList[current][1] = empty
                current = None
            else:
                current = linkedList[current][1]

def deleteItem(item):

    current = head
    previous = head - 1

    while current != None:
        if linkedList[current][0] == item:
            linkedList[previous][1] = linkedList[current][1] # copies previous
            linkedList[current][0] = None
        else:
            previous = current
            current = linkedList[current][1]
            
def getEmpty():

    for i in range(0, len(linkedList)):
        if linkedList[i][0] == None:
            return i


traverse()
addItem("Zhandos")
deleteItem("Sarah")
traverse()