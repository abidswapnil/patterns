# Alpha-Ramp Pattern

class P:
  def makePattern(self, n: int):
    s, res = '', ''
    
    for i in range(n):
      for j in range(i + 1):
        s += chr(65 + i) + ' '
      res += s + '\n'
      s = ''
    
    return res


s = P()
print(s.makePattern(n=10))

# A
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F
# G G G G G G G
# H H H H H H H H
# I I I I I I I I I
# J J J J J J J J J J
