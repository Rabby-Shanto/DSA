from array import *

# 1. Create an array and traverse. 

arr1 = array('i',[1,2,3,4,5,6,7,9])
def oneD_perform(my_array,index,value):
    for i in my_array:
        print(i)
# 2. Access individual elements through indexes
    if index >= len(my_array):
        print("Index out of range")
    else:
        print(my_array[index])
# 3. Append any value to the array using append() method
    my_array.append(value)
    print(my_array)
# 4. Insert value in an array using insert() method
    my_array.insert(0,0)
    print(my_array)
# 5. Extend python array using extend() method
    arr2 = array('i',[15,16,17,18])   
    my_array.extend(arr2)
    print(my_array)
# 6. Add items from list into array using fromlist() method
    temp = [20,21,22]
    
    my_array.fromlist(temp)
    print(my_array)
# 7. Remove any array element using remove() method
    
    my_array.remove(value)
    print(my_array)
# 8. Remove last array element using pop() method
    
    my_array.pop()
    print(my_array)
# 9. Fetch any element through its index using index() method
    
    print(my_array.index(15))
# 10. Reverse a python array using reverse() method
    
    my_array.reverse()
    print(my_array)
# 11. Get array buffer information through buffer_info() method
    my_array.buffer_info()
    print(my_array)
# 12. Check for number of occurrences of an element using count() method
    my_array.append(20)   
    my_array.count(20)
    print(my_array)
# 13. Convert array to string using tostring() method
    str_temp = my_array.tobytes()
    print(str_temp)
    ints = array('i')
    ints.frombytes(str_temp)
    print(ints)

# 14. Slice Elements from an array
    print(my_array[1:4])



oneD_perform(arr1,4,10)