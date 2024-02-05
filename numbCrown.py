# Number Crown Pattern
class P:
  def makePattern(self, n:int):
    s, t, res = '', '', ''
    
    for i in range(n):
      for j in range(i+1):
        s += str(j+1)
      t = s+' '*2*(n-i-1)+s[::-1]
      res += t+'\n'
      s = ''
      
    return res

s = P()
print(s.makePattern(n=9))

1                1
12              21
123            321
1234          4321
12345        54321
123456      654321
1234567    7654321
12345678  87654321
123456789987654321
