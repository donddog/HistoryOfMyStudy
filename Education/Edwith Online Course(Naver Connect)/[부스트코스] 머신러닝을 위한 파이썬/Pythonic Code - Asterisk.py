def asterisk_test(a, *args):
    print(a, args)
    print(type(args))
print()
print(asterisk_test(1,2,3,4,5,6))
print()
'''
1 (2, 3, 4, 5, 6)
<class 'tuple'>
None
'''

def asterisk_test(a, **kargs):
    print(a, kargs)
    print(type(kargs))
print()
print(asterisk_test(1, b=2, c=3, d=4, e=5, f=6))
print()
'''
1 {'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
<class 'dict'>
None
'''

def asterisk_test(a, *args):
    print(a, args[0])
    print(type(args))
print()
print(asterisk_test(1, (2, 3, 4, 5, 6)))
'''
1 (2, 3, 4, 5, 6)
<class 'tuple'>
None
'''

def asterisk_test(a, args):
    print(a, *args)
    print(type(args))
print()
print(asterisk_test(1, (2,3,4,5,6)))
print()
'''
1 2 3 4 5 6
<class 'tuple'>
None
'''

a, b, c = ([1, 2], [3, 4], [5, 6])
print(a, b, c)
print()
'''
[1, 2] [3, 4] [5, 6]
'''

data = ([1, 2], [3, 4], [5, 6])
print(*data)
print()
'''
[1, 2] [3, 4] [5, 6]
'''

for data in zip(*([1, 2], [3, 4], [5, 6])):
    print(sum(data))
print()
'''
9
12
'''

def asterisk_test(a, b, c, d, e=0):
    print(a, b, c, d, e)
print()
'''
10 3 2 1 56
'''

data = {"d":1 , "c":2, "b":3, "e":56}
print(asterisk_test(10, **data))
'''
None
'''