# Symmetric-Butterfly Pattern

class P:
  def makePattern(self, n: int):
    s, res, prev, rng = '', '', 2 * (n - 1), 0
    
    for i in range(n):
      rng = 2 * (i + 1)
      
      for j in range(rng):
        s += '*'
        if j == rng // 2 - 1: s += ' ' * prev
      
      if rng: res += s + '\n'
      prev -= 2
      s = ''
    
    return res + res[:-2 * n - 2][::-1]


s = P()
print(s.makePattern(n=10))

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
# *********  *********
# ********    ********
# *******      *******
# ******        ******
# *****          *****
# ****            ****
# ***              ***
# **                **
# *                  *
