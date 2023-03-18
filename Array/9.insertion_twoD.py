import numpy as np


twoDarr = np.array([[1,2,5,7],[4,6,9,15],[3,7,5,8],[13,16,21,25]])

newtwoDarr = np.insert(twoDarr,0,[[31,41,29,56]],axis=1)
print(newtwoDarr)

# parameters of insert(name_of_array_to_insert,index,new_array,axis=0 indicates rows or 1 indicates coloumn)