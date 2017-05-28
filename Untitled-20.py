# Your Code Here
def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
applyToEach(testList, abs)        