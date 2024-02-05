# Reverse Letter Triangle Pattern

class P:
  def makePattern(self, n: int):
    s, res = '', ''
    
    for i in range(n, -1, -1):
      for j in range(i + 1):
        s += chr(64 + j + 1) + ' '
      res += s + '\n'
      s = ''
    
    return res


s = P()
print(s.makePattern(n=10))

# A B C D E F G H I J K
# A B C D E F G H I J
# A B C D E F G H I
# A B C D E F G H
# A B C D E F G
# A B C D E F
# A B C D E
# A B C D
# A B C
# A B
# A
