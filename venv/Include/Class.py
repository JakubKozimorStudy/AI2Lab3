def variadic(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

variadic(2, 3, 5, 7)
variadic(1, 1, n=1)
try:
    variadic(eval('n=1, 2, 3'))
except SyntaxError:
    print("SyntaxError")
variadic()
variadic(cs="Computer Science", pd="Product Design")
try:
    variadic(eval('cs="Computer Science", cs="CompSci", cs="CS"'))
except SyntaxError:
    print("SyntaxError")
variadic(5, 8, k=1, swap=2)
variadic(8, *[3, 4, 5], k=1, **{'a':5, 'b':'x'})
variadic(*[8, 3], *[4, 5], k=1, **{'a':5, 'b':'x'})
variadic(*[3, 4, 5], 8, *(4, 1), k=1, **{'a':5, 'b':'x'})
variadic({'a':5, 'b':'x'}, *{'a':5, 'b':'x'}, **{'a':5, 'b':'x'})