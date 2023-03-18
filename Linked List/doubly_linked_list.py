 # Doubly Linked List

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None 

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    #  Creation of Doubly Linked List
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL is created Successfully"

    def insertDLL(self,value,location):
        if self.head is None:
            return "Double linked list doesn't exists!"
        else:
            node = Node(value)
            if location == 0:
                node.prev = None
                node.next = self.head
                self.head.prev = node
                self.head = node
            elif location == 1:
                node.next = None
                node.prev = self.tail
                self.tail.next = node
                self.tail = node
            
            else:
                index = 0
                tempNode = self.head

                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                node.next = tempNode.next
                node.prev = tempNode
                node.next.prev = node
                tempNode.next = node





dLinkedlist = DoublyLinkedList()

dLinkedlist.createDLL(5)

dLinkedlist.insertDLL(1,0)
dLinkedlist.insertDLL(4,1)
dLinkedlist.insertDLL(3,0)
dLinkedlist.insertDLL(5,2)

print([node.value for node in dLinkedlist])


