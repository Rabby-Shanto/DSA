class Stack:
    def __init__(self, *args, **kwargs):
        self.stack = []
        self.minStack = []

    def push(self,val):
        self.stack.append(val)
        val = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self):
        self.stack.pop()
        self.minStack.pop()
    
    def top(self):
        return self.stack[-1]

    def minVal(self):
        return self.minStack[-1]



minimumStack = Stack()
minimumStack.push(2)
minimumStack.push(4)
minimumStack.push(5)
minimumStack.pop()
print(minimumStack.top())
print(minimumStack.minVal())

