start = 0; end = 0;
large = 0
ls = []
for x in range(len(s)):
  if s[x] >= s[x-1] and x!=(len(s)-1):
    continue
  elif x == (len(s)-1):
    if s[x] >= s[x-1]: 
     end = x 
     if (end-start+1)> large:
       large = end-start
       a = start
       b = end+1
     start = end
    else:
      end = x 
      if (end-start)> large:
        large = end-start
        a = start
        b = end 
      start = end 
  else:
    end = x 
    if (end-start)> large:
      large = end-start
      a = start
      b = end 
    start = end 
print(s[(a):(b)])    