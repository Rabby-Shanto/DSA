


# create stack list


class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    

    def isEmpty(self):

        if self.list == []:
            return True
        else:
            return False
        
    def push(self,value):

        self.list.append(value)

        return self.list
    

    def pop(self):

        if self.list == []:
            return "There is no element to pop out"
        
        else:
            return self.list.pop()
        

    def peek(self):

        if self.list == []:
            return "there is no element in the stack"
        
        else:
            return self.list[len(self.list) - 1]
        
    def delete(self):

        self.list = None

    

customList = Stack()

customList.push(1)
customList.push(2)
customList.push(3)
customList.push(4)

print(customList)

print(customList.isEmpty())

