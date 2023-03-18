# Remove elements from array


from array import *

arr1 = array('i',[3,6,9,12,15,20])

arr1.remove(12)
print(arr1)

# Discussion about complexity


'''

to count time complexity,In this array it will be O(n) because,\
array can't hold blank space in memory.so,if an element is being removed,other elements next to the removed\
other element's next to the removed element will be shifted forward to the blank memory space,So,every\
element next will be shifted too,So,time complexity will be O(n),if the last element is removed,then there\
will be O(1) complexity because there we don't need to shift other elements

and Space complexity will be O(1) because we don't require extra memory space to perform this action


'''
