def oddTuples(aTup):
 c = 0
 ls = []
 for x in aTup:
  if c%2==0:
  	ls.append(x)	
  c+=1 
 return tuple(ls)
#aTup = ('apple',534,'dffdf',54,'rtr')
#print(oddTuple(aTup))