# array queue[5]
loop = True
queue = [0,0,0,0,0]
front = 0
rear = -1
size = 0

def enQueue(item): # add to the back of the queue
    global size, rear, queue
    size += 1
    if size > 5: # as we are working with an array, it cannot go beyond a fixed length
        print("\nERR: Queue full.")
    else:
        rear = (rear + 1)%5
        queue[rear] = item

def deQueue(): # remove from the front of the queue
    global size, front, queue
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

# fix weird bug where you have to remove twice in order to add to a full list.