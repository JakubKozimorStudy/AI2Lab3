def all_together(x, y, z=1, *nums, indent=True, spaces=4, **options):
    print("x:", x)
    print("y:", y)
    print("z:", z)
    print("nums:", nums)
    print("indent:", indent)
    print("spaces:", spaces)
    print("options:", options)


try:
    all_together(2)
except TypeError:
    print("TypeError")
all_together(2, 5, 7, 8, indent=False)
all_together(2, 5, 7, 6, indent=None)
try:
    all_together()
except TypeError:
    print("TypeError")
try:
    all_together(eval('indent=True, 3, 4, 5'))
except SyntaxError:
    print("SyntaxError")
try:
    all_together(**{'indent': False}, scope='maximum')
except TypeError:
    print("TypeError")
all_together(dict(x=0, y=1), *range(10))
try:
    all_together(eval('**dict(x=0, y=1), *range(10)'))
except SyntaxError:
    print("SyntaxError")
try:
    all_together(*range(10), **dict(x=0, y=1))
except TypeError:
    print("TypeError")
try:
    all_together([1, 2], {3: 4})
except TypeError:
    print("TypeError")
try:
    all_together(8, 9, 10, *[2, 4, 6], x=7, spaces=0, **{'a': 5, 'b': 'x'})
except TypeError:
    print("TypeError")
all_together(8, 9, 10, *[2, 4, 6], spaces=0, **{'a': [4, 5], 'b': 'x'})
all_together(8, 9, *[2, 4, 6], *dict(z=1), spaces=0, **{'a': [4, 5], 'b': 'x'})
