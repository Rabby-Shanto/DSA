# Singly Linked List

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Slinkedlist:

    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node #works like return but memory efficient and used to iterate over large 
            node = node.next

    # insertion
    def insertLList(self,value,location):
        newNode = Node(value) #1.creating a new node and initialize value to it

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:

            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempNode = self.head
                pointer = 0

                while pointer < location - 1:
                    tempNode = tempNode.next
                    pointer += 1

                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    # Traverse in Singly Linked List

    def traverseSLList(self):

        if self.head is None:
            print("Singly Linked List doesn't exist")
        else:
            node = self.head

            while node:
                print(node.value)
                node = node.next

    def searchLList(self,val):
        if self.head is None:
            print("Singly Linked List doesn't exists!")

        else:
            node = self.head

            while node:
                if node.value == val:
                    return node.value
                node = node.next

            return "Value doesn't exists in linked list"

    def DeleteLList(self,location):
        if self.head is None:
            print("Singly Linked List doesn't exists!")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node

            else:
                tempnode = self.head
                index = 0

                while index < location -1:
                    tempnode = tempnode.next
                    index += 1

                nextnode = tempnode.next

                tempnode.next = nextnode.next


    # Delete entire linked list
    def DelSList(self):
        if self.head is None:
            print("Singly Linked List doesn't exists!")

        else:
            self. head = None
            self.tail = None




SinglyLlist = Slinkedlist()
SinglyLlist.insertLList(1,1)
SinglyLlist.insertLList(2,1)
SinglyLlist.insertLList(3,1)
SinglyLlist.insertLList(5,1)
SinglyLlist.insertLList(0,1)
SinglyLlist.insertLList(8,1)
SinglyLlist.insertLList(4,1)
SinglyLlist.insertLList(2,1)
print([node.value for node in SinglyLlist])

# SinglyLlist.traverseSLList()
# print(SinglyLlist.searchLList(6))

SinglyLlist.DeleteLList(0)
print([node.value for node in SinglyLlist])

SinglyLlist.DelSList()
print([node.value for node in SinglyLlist])

