def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    c,large = 0,0;new = 's'
    key = []
    key = aDict.keys()
    for word in key:
      c = len(aDict[word])
      if c>large:
        large = c 
        new = word
    return new   