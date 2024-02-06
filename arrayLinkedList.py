linkedList = [
    ["Bob", 3],
    ["Sarah", 2],
    ["Shanon", None],
    ["Roberto", 1],
    [None,None],
    [None,None]
]

head = 0

def traverse():
    
    current = head

    while current != None:
        print(linkedList[current][0])
        current = linkedList[current][1]

def addItem(item):

    current = head

    while current != None:
        if linkedList[current][1] == None:
            empty = getEmpty()
            linkedList[empty][0] = item
            linkedList[current][1] = empty
            current = linkedList[current][1]
        
def getEmpty():

    for i in range(0, len(linkedList)):
        if linkedList[i][0] == None:
            return i


traverse()
addItem("Zhandos")
traverse()