def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    result = 1
    x = 1
    while(x<=a):
     if(a%x==0 and b%x==0):
      result = x
     x+=1 
    return result