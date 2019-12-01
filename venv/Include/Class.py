def keyword_args(a, b=1, c='X', d=None):
    print("a:", a)
    print("b:", b)
    print("c:", c)
    print("d:", d)


keyword_args(5)
keyword_args(a=5)
keyword_args(5, 8)
keyword_args(5, 2, c=4)
keyword_args(5, 0, 1)
keyword_args(5, 2, d=8, c=4)
try:
    keyword_args(5, 2, 0, 1, "")
except TypeError:
    print("TypeError")
try:
    keyword_args(eval('c=7, 1'))
except SyntaxError:
    print("SyntaxError")
keyword_args(c=7, a=1)
keyword_args(5, 2, [], 5)
try:
    keyword_args(1, 7, e=6)
except TypeError:
    print("TypeError")
keyword_args(1, c=7)
try:
    keyword_args(5, 2, b=4)
except TypeError:
    print("TypeError")