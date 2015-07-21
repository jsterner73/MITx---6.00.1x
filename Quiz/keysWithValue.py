def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    myList = []
    for key, value in aDict.iteritems():
        if (value == target):
            myList.append(key)
            
    return sorted(myList)