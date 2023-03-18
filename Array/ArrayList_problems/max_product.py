# get max product of two integers in array where all elements are positive


import numpy as np

arr = np.array([1,3,5,7,12,18,21])

def maxProduct(nums):
    max_product = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] * nums[j] > max_product:
                max_product = nums[i] * nums[j]
                pairs = str(nums[i]) + ',' + str(nums[j])
                

    print(max_product)
    print(pairs)


maxProduct(arr)