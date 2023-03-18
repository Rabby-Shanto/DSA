# get the kth element from the last node

from LinkedList import LinkedList



def KthLast(linkedlist,n):
    pointer1 = linkedlist.head
    pointer2 = linkedlist.head

    for i in range(n):
        if pointer2 is None:
            return None

        pointer2 = pointer2.next
    while pointer2:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    
    return pointer1


customLL = LinkedList()

customLL.randomNum(10,0,18)
print(customLL)

print(KthLast(customLL,5))
