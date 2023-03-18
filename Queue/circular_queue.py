class Queue:

    def __init__(self,maxsize):

        self.items = maxsize * [None]
        self.maxsize = maxsize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        

        if self.start == self.top + 1:
            return True
        
        elif self.start == 0 and  self.top + 1 == self.maxsize:
            return True
        else:
            return False
        
    def isEmpty(self):
        if self.top == -1:
            return True
        
        else:
            return False
        
    def enqueue(self,value):
        if self.isFull():
            return "the queue is full"
        
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0

            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0

            self.items[self.top] = value

            return "added"
            



customQueue = Queue(3)

customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)

print(customQueue)
print(customQueue.isFull())