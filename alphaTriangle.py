# Alpha-Triangle Pattern

class P:
  def makePattern(self, n: int):
    s, res = '', ''
    
    for i in range(n):
      for j in range(i + 1):
        s += chr(65 + n - 1 - i + j) + ' '
      res += s + '\n'
      s = ''
    
    return res


s = P()
print(s.makePattern(n=10))

# J
# I J
# H I J
# G H I J
# F G H I J
# E F G H I J
# D E F G H I J
# C D E F G H I J
# B C D E F G H I J
# A B C D E F G H I J
