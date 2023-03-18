# Array Insertion

# 1. To insert elements in array,There are two things need to know:
# ---> insert to the beginning of array: here if we want to insert element at the beginning of the array a[0],\
#     we need to move all others element in the array.As we have to move all elements in the array.So,the time\
#     complexity will be O(n).Now,if we have fixed array size,a new array will be created with large array size\
#     and array elements will be moved to new array.The time complexity will be same as before

# ---> insert at the end of the array: to insert a element at the end of the array,we don't need to move all\
#     the elements in the array.So,the complexity will be O(1)

from array import *

arr1 = array('i',[5,7,8,10,20])

arr1.insert(0,2)

print(type(arr1))
print(arr1)