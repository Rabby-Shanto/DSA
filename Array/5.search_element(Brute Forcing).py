from array import *

arr1 = array('i',[1,2,3,4,5,6])

def search_arr(array,target):
    for i in array:
        if i == target:
            return array.index(target)

    return f"element not found"

print(search_arr(arr1, 6))

# time complexity O(n)
