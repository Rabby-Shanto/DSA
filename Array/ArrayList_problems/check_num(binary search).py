# checking if a number is exist in sorted array through binary search


import numpy as np

arr = np.array([13,18,19,21,15])

def checkNum(nums,val):
    left = 0
    right = len(nums)-1
    mid = 0

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] < val:
            left = mid + 1
        elif nums[mid] > val:
            right = mid - 1
        else:
            return mid

    return "element not present"

print(checkNum(arr,21))


