loop = True
queue = [0,0,0,0,0] # array queue[5]
front = 0
rear = -1
size = 0

def enQueue(item): # add to the back of the queue
    global size, rear, queue
    if size == 5: # we are working with an array which has a static length of 5
        print("\nERR: Queue full.")
    else:
        size += 1
        rear = (rear + 1)%5
        queue[rear] = item

def deQueue(): # remove from the front of the queue (whilst not actually removing any array elements in memory
    global size, front
    size -= 1
    front = (front + 1)%5

while loop:
    choice = input("\nAdd [1]\nRemove [2]\nQuit [3]\n\nENTER: ") # the user can either remove or add from the queue
    if choice == '1':
        item = int(input("\nENTER: "))
        enQueue(item)
        print(queue)
    elif choice == '2':
        deQueue()
        print(size)
        print(queue)
    else:
        loop = False
