import numpy as np


twoDarr = np.array([[1,2,5,7],[4,6,9,15],[3,7,5,8],[13,16,21,25]])


def accessElement(array,row_index,col_index):
    if row_index >= len(array) and col_index >= len(array[0]):
        return "array index out of range"
    return array[row_index][col_index]

print(accessElement(twoDarr,2,3))