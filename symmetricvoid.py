# Symmetric-Void Pattern

class P:
  def makePattern(self, n: int):
    s, res, prev, rng = '', '', 0, 0
    
    for i in range(n):
      rng = 2 * n - 2 * i
      
      for j in range(rng):
        s += '*'
        if j == (rng // 2) - 1: s += ' ' * prev
      
      if rng: res += s + '\n'
      prev += 2
      s = ''
    
    return res + res[:-2 * n - 2][::-1]


s = P()
print(s.makePattern(n=10))

# ********************
# *********  *********
# ********    ********
# *******      *******
# ******        ******
# *****          *****
# ****            ****
# ***              ***
# **                **
# *                  *
# *                  *
# **                **
# ***              ***
# ****            ****
# *****          *****
# ******        ******
# *******      *******
# ********    ********
# *********  *********
# ********************
