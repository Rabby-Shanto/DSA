class MyQueue:

    def __init__(self):
        self.inStack = []
        self.outStack = []
        

    def push(self, x: int) -> None:
        self.inStack.append(x)
        

    def pop(self) -> int:
        while len(self.inStack):
            self.outStack.append(self.inStack.pop())
        result = self.outStack.pop()
        while len(self.outStack):
            self.inStack.append(self.outStack.pop())
        return result
        

    def peek(self) -> int:
          return self.inStack[0]

    def empty(self) -> bool:
        return len(self.inStack) == 0