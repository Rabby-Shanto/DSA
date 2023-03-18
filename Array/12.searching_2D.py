import numpy as np


twoDarr = np.array([[1,2,5,7,9],[4,6,9,15,11],[3,7,5,8,13],[13,16,21,25,20]])

def traverse_2D(array,target):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j]== target:
                return "this value is located at index "+str(i)+' '+str(j)
    return "array element not found"

print(traverse_2D(twoDarr,15))

