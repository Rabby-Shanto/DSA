# accessing element from array

from array import *



def acces_element(array,index):

    if index >= len(array): 
        print("Index out of range")
    else:
        print(array[index])

p = acces_element([1,2,3,6,7,8],8)

# time complexity = O(1)