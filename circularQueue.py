# array queue[5]
loop = True
queue = [0,0,0,0,0]
front = 0
rear = -1
size = 0

def enQueue(item):
    global size, rear, queue
    size += 1
    if size == 6:
        print("\nERR: Queue full.")
    else:
        rear = (rear + 1)%5
        queue[rear] = item

def deQueue():
    global size, front, queue
    size -= 1
    front = (front + 1)%5

while loop:
    choice = input("\nAdd [1]\nRemove [2]\nQuit [3]\n\nENTER: ")
    if choice == '1':
        item = int(input("\nENTER: "))
        enQueue(item)
        print(queue)
    elif choice == '2':
        deQueue()
        print(queue)
    else:
        loop = False