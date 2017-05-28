app = 0
for x in range(len(s)):
 if( x == 0 or x== 1):
   continue
 if(s[x-2] == 'b' and s[x-1]=='o' and s[x] == 'b'):
   app +=1
print("Number of times bob occurs is:",app)
