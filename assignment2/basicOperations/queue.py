import math

# stack implementation
# without using any in built functions - NO BUILT IN FUNCTIONS

class OperationsQueue():

    def __init__(self):
        self.queue = []
        self.pointerFront = -1
        self.pointerBack = 0
        self.length = 0

    def initQueue(self, queue):
        self.queue = queue
        self.pointerFront = len(queue) - 1
        self.pointerBack = 0
        self.length = self.lengthQueue()


    def lengthQueue(self):
        return self.pointerBack + self.pointerFront + 1

    def putBackOfQueue(self, element):

        elementNew = [element]

        for i in self.queue:
            elementNew.append(i)

        self.queue = elementNew

    
    def getElementFront(self):
        return self.queue[self.pointerFront]
        
    
    def popFront(self):
        self.pointerFront += 1

    def popBack(self):
        self.pointerBack -= 1

    def getAllElements(self):
        return self.queue[self.pointerFront:self.pointerBack]




operations_stack = OperationsQueue()

operations_stack.initQueue([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(operations_stack.lengthQueue())

operations_stack.putBackOfQueue(44)
operations_stack.getElementFront()
operations_stack.popFront()
print(operations_stack.getAllElements())
