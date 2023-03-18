# array declaration in python 
# python don't support array data structure by default,We need to import array to use
# array support only one datatype at a time like we can't use integer and float in same array
# array elements in memory are one dimensional,we may have 3D or Multi-D array \
# and in memory they are represented as one dimensional

from array import *

arr1 = array('i',[5,7,2,8,15])
arr2 = array('d',[5.2,7.5,2.3,8.1,15.1])

print(arr1)
print(arr2)