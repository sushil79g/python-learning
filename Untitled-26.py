def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ',len(secretWord),' letters long')
    
    length = len(secretWord)
    d = []
    neww = []
    neww = list(secretWord)
    lettersGuessed = []
    c = 0
    #print('there are ',length,' letters')
    for x in range(0,8,1):
        print('-----------')
        print('You have',8-c,'guesses left')
        print('Available Letters:',getAvailableLetters(lettersGuessed))
        le = input("Please guess a letter:")
        le = le.lower()
        #new = []
        
        if len(le)>1:
            print("enter only one letter")
            continue
        
            
           
        
        lettersGuessed.append(le)
        if le in neww:
          print('Good guess:',getGuessedWord(secretWord,lettersGuessed))
        elif le in d:
          print('Oops! You \'ve already guessed that letter:',getGuessedWord(secretWord,lettersGuessed))
      
        else:
          print('Oops! That letter is not in my word:',getGuessedWord(secretWord,lettersGuessed))
          c = c + 1
        d = lettersGuessed[:]
        if isWordGuessed(secretWord, lettersGuessed):
            print('-----------')
            print("Congratulations, you won!")
            #print('None')
            return ()
        #for latt in secretWord:
        for xyz in  neww:
         if le in neww:
           neww.remove(le)
            
    print('-----------')
    print('Sorry, you ran out of guesses. The word was',secretWord) 