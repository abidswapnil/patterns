# Binary Number Triangle Pattern

class P:
  def makePattern(self, n:int):
    s, res = '', ''
    
    for i in range(n):
      for j in range(i+1):
        if i % 2: s += '1 ' if j%2 else '0 '
        else: s += '0 ' if j%2 else '1 '
      res += s+'\n'
      s = ''
      
    return res

s = P()
print(s.makePattern(n=10))


1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1 
1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 
1 0 1 0 1 0 1 0 1 
0 1 0 1 0 1 0 1 0 1 
