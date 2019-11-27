def print_two(a, b):
    print("Arguments: {0} and {1}".format(a, b))

try:
    print_two(4, 1, b=1)
except TypeError:
    print("Wrong type")
try:
    print_two(1, a=1)
except TypeError:
    print("Wrong type")
try:
    print_two(b=1, a=4)
except TypeError:
    print("Wrong type")
try:
    print_two(a=4, b=1)
except TypeError:
    print("Wrong type")
try:
    print_two(eval('b=4, 1'))
except SyntaxError:
    print("Wrong syntax")
try:
    print_two(4, a=1)
except TypeError:
    print("Wrong type")
try:
    print_two(4, 1, 1)
except TypeError:
    print("Wrong type")
try:
    print_two(4, a=1)
except TypeError:
    print("Wrong type")
try:
    eval('print_two(a=4, 1)')
except SyntaxError:
    print("Wrong syntax")
try:
    print_two(41)
except TypeError:
    print("Wrong type")
try:
    print_two(4,1)
except TypeError:
    print("Wrong type")
try:
    print_two()
except TypeError:
    print("Wrong type")
