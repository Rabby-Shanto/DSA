
# use a single list to implement three stacks

class MultiStack:
    def __init__(self,stackSize):
        self.numStack = 3
        self.stackList = [0]*(stackSize * self.numStack)
        self.sizes = [0] * self.numStack
        self.stackSize = stackSize

    def isFull(self,stackNum):
        if self.sizes[stackNum] == self.stackSize:
            return True
        else:
            return False
        
    def isEmpty(self,stackNum):
        if self.sizes[stackNum] == 0:
            return True
        else:
            return False


stack = MultiStack()