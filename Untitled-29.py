def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    for latter in word:
        if latter not in hand.keys():
            return False
        elif word.count(latter)>hand[latter]:
            return False
    if word not in wordList:
        return False
    return True  