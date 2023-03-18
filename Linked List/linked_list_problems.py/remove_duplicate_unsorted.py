# remove duplicate from unsorted Linked List

import os
from LinkedList import LinkedList
    
def remove_dups(linkedlist):

    if linkedlist.head is None:
        return "linked list have no head value"

    else:
        tempNode = linkedlist.head
        tempValue = set([tempNode.value])

        while tempNode.next:
            if tempNode.next.value in tempValue:
                tempNode.next = tempNode.next.next

            else:
                tempValue.add(tempNode.next.value)
                tempNode = tempNode.next
        
        return linkedlist


customLL = LinkedList()

customLL.randomNum(10,0,16)
print(customLL)
remove_dups(customLL)
print(customLL)