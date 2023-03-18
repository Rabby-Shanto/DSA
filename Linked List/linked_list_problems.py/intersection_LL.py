
# intersecting node


from LinkedList import LinkedList,Node


def intersectNode(llA,llB):
    if llA.tail is not llB.tail:
        return False

    lenA = len(llA)
    lenB = len(llB)

    shorter = llA if lenA<lenB else llB
    longer = llB if lenA<lenB else llA

    diff = len(longer) - len(shorter)

    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next

    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next
    
    return longerNode


def addsameNode(llA,llB,value):
    tempNode = Node(value)

    llA.tail.next = tempNode
    llA.tail = tempNode
    llB.tail.next = tempNode
    llB.tail = tempNode


llA = LinkedList()
llA.randomNum(3,0,10)
llB = LinkedList()
llB.randomNum(4,0,10)

addsameNode(llA,llB,11)
addsameNode(llA,llB,14)

print(llA)
print(llB)

print(intersectNode(llA,llB))