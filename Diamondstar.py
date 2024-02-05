# Diamond Star Pattern

class P:
  def makePattern(self, n:int):
    s, res, k = '', '', 1
    
    for i in range(2*n):
      if i > n: k += 4
      j = 2 * i + 1 if i < n else 2 * i - k
      for _ in range(j):
        s += '*'
      res += ' '*((2*n-j)//2)+s+'\n'
      s = ''
    return res

s = P()
print(s.makePattern(n=10))

#          *
#         ***
#        *****
#       *******
#      *********
#     ***********
#    *************
#   ***************
#  *****************
# *******************
# *******************
#  *****************
#   ***************
#    *************
#     ***********
#      *********
#       *******
#        *****
#         ***
#          *
