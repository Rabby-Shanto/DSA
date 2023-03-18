
# circular singly linked List

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class CircularSlinkedlist:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node #works like return but memory efficient and used to iterate over large 
            node = node.next
            if node == self.tail.next:
                break

    def createSinglyCLList(self,nodeValue):
            node = Node(nodeValue)
            node.next = node
            self.head = node
            self.tail = node

            return "Singly Circular Linked List created"

    def insertSList(self,value,location):
        
        if self.head is None:
            return "head node none"
        else:
            newNode = Node(value)
            
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == 1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0

                while index < location-1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "Node has been successfully inserted!"

    def traverseCSList(self):
        if self.head is None:
            return "head node doesn't exists!"
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode= tempNode.next

                if tempNode == self.tail.next:
                    break

    def searchCSList(self,nodeValue):

        if self.head is None:
            return "head doesn't exists"
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == nodeValue:
                    return tempnode.value
                tempnode = tempnode.next

                if tempnode == self.tail.next:

                    return "value doesn't exists in Linked List"

    
    def removeNode(self,location):
        if self.head is None:
            return "no Head node!"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == 1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    tempNode = self.head
                    while tempNode:
                        if tempNode.next == self.tail:
                            break
                        tempNode = tempNode.next
                    tempNode.next = self.head
                    self.tail = tempNode

            else:
                index = 0
                tempNode = self.head
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.node



circularSlist = CircularSlinkedlist()
circularSlist.createSinglyCLList(1)

circularSlist.insertSList(1,0)
circularSlist.insertSList(2,0)
circularSlist.insertSList(1,1)
circularSlist.insertSList(3,0)
circularSlist.insertSList(4,2)
circularSlist.traverseCSList()
print([node.value for node in circularSlist])
print(circularSlist.searchCSList(5))