def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    ind = 0
    secretWor = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    remain = []
    for latter in secretWor:
       if latter not in lettersGuessed:
          remain.append(latter)
    sec = ''.join(sorted(remain))
    return sec