def updateHand(hand, word):
  uhand = hand.copy()
  for element in word:
        if element in uhand:
            if uhand[element]>0:
                uhand[element] -=1
  return uhand