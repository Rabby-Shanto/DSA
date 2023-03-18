
myDict = {'name' : 'shanto', 'age' : 28, 'hobby' : 'coding'}

def addDict(dict,key,value):

    dict[key] = value

    return dict

# adding key-val to dict
print(addDict(myDict,'school','nstu'))

# updating value
myDict['school'] = 'CZS'

print(myDict)
