# Increasing Number Triangle Pattern

class P:
  def makePattern(self, n:int):
    s, res, prev = '', '', 1
    
    for i in range(n):
      j = i+1
      for _ in range(j):
        s += str(prev)+' '
        prev += 1
      res += s+'\n'
      s = ''
    return res

s = P()
print(s.makePattern(n=10))


1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
16 17 18 19 20 21 
22 23 24 25 26 27 28 
29 30 31 32 33 34 35 36 
37 38 39 40 41 42 43 44 45 
46 47 48 49 50 51 52 53 54 55 
