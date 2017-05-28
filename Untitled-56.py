def genPrimes(n):
    for x in range(2,1000):
        for y in range(2,x):
            if y%x==0:
                break
            else:
                yield x
                break