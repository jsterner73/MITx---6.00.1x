def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    myList = []
    for item in aList:
        if len(item) < 4:
            myList.append(item)
    return myList