# partition of linked list


from LinkedList import LinkedList


def partition_list(ll,nodeValue):
    currNode = ll.head
    ll.tail = ll.head

    while currNode:
        nextNode = currNode.next
        currNode.next = None
        if currNode.value < nodeValue:
            currNode.next = ll.head
            ll.head = currNode
        else:
            ll.tail.next = currNode
            ll.tail = currNode
        currNode = nextNode

    if ll.tail.next is not None:

        ll.tail.next = None



ptList = LinkedList()

ptList.randomNum(10,0,99)
print(ptList)
partition_list(ptList,50)
print(ptList)

