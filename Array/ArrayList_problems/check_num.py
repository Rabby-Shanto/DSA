# check an array if it contains a certain number or not


import numpy as np


arr = np.array([1,2,3,4,5,6,7,8,9,20])


def checkNum(nums,val):
    for i in nums:
        if i == val:
            return True
    return False

print(checkNum(arr,10))