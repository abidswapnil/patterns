# Rectangular Star Pattern
class P:
  def makePattern(self, n: int):
    s, res = '', ''
    
    for i in range(n):
      for _ in range(n if not i or i is n-1 else 2):
        s += '*' if not i or i is n-1 else '*'+' '*(n-2)
      res += s + '\n'
      s = ''
    return res


s = P()
print(s.makePattern(n=10))

# **********
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# *        *
# **********