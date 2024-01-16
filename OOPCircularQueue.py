'''
This code is essentially 'circularQueue.py' but using OOP. An array that acts as a circular queue of 5 elements is created
that the user is able to add and remove from.
'''

class Circular_Queue():
   
    def __init__(self):
        self.front = 0
        self.rear = -1
        self.size = 0

    def enQueue(self, theItem):
        if size == 5:
            print("ERR: Queue full.")