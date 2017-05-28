def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    c = 0
    key = []
    key = aDict.keys()
    for word in key:
      c = c + len(aDict[word])
    return c  
