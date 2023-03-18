class Plates:
    def __init__(self,capacity):
        self.capacity = capacity
        self.stacks = []


    def push(self,item):
        if len(self.stacks)>0 and len(self.stacks[-1])<self.capacity:
            return self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    def pop(self):
        while len(self.stacks) and len(self.stacks[-1])==0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        else:
            return self.stacks[-1].pop()
        
    def pop_at(self,stackIndex):
        if len(self.stacks[stackIndex]) > 0:
            return self.stacks[stackIndex].pop()
        else:
            return None
        

stack_pl = Plates(2)

stack_pl.push(1)
stack_pl.push(2)
stack_pl.push(3)
stack_pl.push(4)
stack_pl.push(5)
stack_pl.pop_at(0)
stack_pl.push(20)


