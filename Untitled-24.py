def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    ind = 0
    secretWor = []
    secretWor = list(secretWord)
    #print(secretWor)
    for latter in secretWor:
      if latter not in lettersGuessed:
        ind = secretWor.index(latter)
        secretWor[ind]= '_'
     
    sec = ''.join(secretWor)
    return sec    
      