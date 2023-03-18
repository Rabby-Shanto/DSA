# Finding the missing number through N-Sum series

myList = [1,2,3,4,5,7,8,9,10]

def Missing_num(list,n):
    sum_total = n*(n+1)/2
    sum_arr = sum(list)
    
    return sum_total-sum_arr

print(Missing_num(myList,10))