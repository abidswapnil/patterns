# Rectangular Star Pattern

class P:
  def makePattern(self, n: int):
    s, res = '', ''
    
    for i in range(n):
      for _ in range(n):
        s += '*'
      res += s + '\n'
      s = ''
    return res


s = P()
print(s.makePattern(n=10))

# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
# **********
