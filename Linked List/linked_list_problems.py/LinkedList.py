# creating linked list class

import random

class Node:
    def __init__(self,value=None):
        self.value = value
        self.prev = None
        self.next = None

    def __str__(self):
        return str(self.value)



class LinkedList:
    def __init__(self,values = None):
        self.head = None
        self.tail = None

    def __iter__(self):
        currNode = self.head

        while currNode:
            yield currNode
            currNode = currNode.next

    
    def __str__(self):
        values = [str(x.value) for x in self]

        return '->'.join(values)
        

    def __len__(self):

        index = 0
        node = self.head

        while node:
            index += 1
            node = node.next
        
        return index

    def add(self,value):
        if self.head is None:
            node = Node(value)
            self.head = node
            self.tail = node

        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

        return self.tail

    def randomNum(self,n,min_value,max_value):
        self.head = None
        self.tail = None

        for i in range(n):
            self.add(random.randint(min_value,max_value))
        return self

# customLL = LinkedList()

# customLL.randomNum(8,0,99)

# print(customLL)
