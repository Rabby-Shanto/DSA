# find the index of list elements where their value is sum of the target value.

#list = [2,4,6,7] target = 8,so output should be list[0 2]

def twoSum(nums,target):
    d = {}

    for i,j in enumerate(nums):
        reminder = target - j
        if reminder in d:return [d[reminder],i]
        d[j] = i

print(twoSum([2,4,6,7],8))