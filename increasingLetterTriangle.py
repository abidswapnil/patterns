# Increasing Letter Triangle Pattern

class P:
  def makePattern(self, n:int):
    s, res = '', ''
    
    for i in range(n):
      for j in range(i+1):
        s += chr(64+j+1)+' '
      res += s+'\n'
      s = ''
      
    return res

s = P()
print(s.makePattern(n=10))


A 
A B 
A B C 
A B C D 
A B C D E 
A B C D E F 
A B C D E F G 
A B C D E F G H 
A B C D E F G H I 
A B C D E F G H I J 
