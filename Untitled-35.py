# Paste your function here
def dotProduct(listA, listB):
  total = 0
  for x in range(len(listA)):
    total += listA[x]*listB[x]
  return total