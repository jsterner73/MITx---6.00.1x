def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    # Your code here
    returnValue = []
    dummyDict = {}
    for key, value in aDict.items():
        if (value not in dummyDict):
            dummyDict[value] = 1
        else:
            dummyDict[value] += 1

    for key, value in aDict.items():
        if (dummyDict[value] == 1):
            returnValue.append(key)
    return sorted(returnValue)
    
aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
print uniqueValues(aDict)
aDict = {1: 1, 2: 1, 3: 1}
print uniqueValues(aDict)