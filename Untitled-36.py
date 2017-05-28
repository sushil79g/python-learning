# Paste your function here
def deep_reverse(L):
  m = L[:]
  for x in range(len(m)):
    m[x] =list(reversed(m[x]))
  m = list(reversed(m))
  L[:]=m[:]