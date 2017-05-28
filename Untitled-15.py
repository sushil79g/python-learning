import math
def polysum(n,s):
 area = 0.25*n*s*s
 area = area/math.tan(math.pi/n)
 perimeter = n*s
 sum = area + perimeter**2
 return round(sum,4)