def calculateHandlen(hand):
 #hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
 #key = hand.keys()
 #return len(key)
 total = 0
 for key in hand.keys():
   total += hand[key]
 return total 