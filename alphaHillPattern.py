# Alpha-Hill Pattern

class P:
  def makePattern(self, n: int):
    s, res, prev = '', '', None
    
    for i in range(n):
      for j in range(2 * i + 1):
        if j <= (2 * i + 1) // 2:
          s += chr(65 + j) + ' '
          prev = 65 + j
        else:
          if prev: s += chr(prev - 1) + ' '
          prev -= 1
      res += ' ' * 2 * (n - i) + s + '\n'
      s = ''
    
    return res


s = P()
print(s.makePattern(n=26))

#                   A
#                 A B A
#               A B C B A
#             A B C D C B A
#           A B C D E D C B A
#         A B C D E F E D C B A
#       A B C D E F G F E D C B A
#     A B C D E F G H G F E D C B A
#   A B C D E F G H I H G F E D C B A
# A B C D E F G H I J I H G F E D C B A
