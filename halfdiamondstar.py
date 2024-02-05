# Half Diamond Star Pattern

class P:
  def makePattern(self, n:int):
    s, res, j, prev = '', '', 0, 0
    
    for i in range(2*n):
      if i > n: prev -= 1
      if i < n: j = i+1
      else: j = prev
      
      for _ in range(j):
        s += '*'
      res += s+'\n'
      s = ''
      
      if i < n: prev = i
    return res

s = P()
print(s.makePattern(n=10))


*
**
***
****
*****
******
*******
********
*********
**********
*********
********
*******
******
*****
****
***
**
*
