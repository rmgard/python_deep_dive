def func1(a, b, c):
    print(a, b, c)

# using keyword aruments does not require order:
def func2(b = 2, c = 3, a = 1):
    print(a, b, c)

# Adding star args with an argument afterwards requires a key arg:
def starArgsPlusKey(a, b, *args, d):
    print(a, b, args, d)

''' In this example * says, "I don't want 
any positional args after this point
'''
def star(*, d):
    print(d)

'''Another * example shows that we can pass some 
    positional args into the function, but they 
    are nixed at the point of *. This example
    requires 2 positional args and NO MORE, then
    a key arg d '''
def posStarKey(a, b, *, d):
    print(a, b, d)

''' Note below how *args collects remaining
    positionals which come after the first
    keyed item "b". This is not intuitive
    since positionals usually are disallowed
    at the point of using your first key arg
    '''
def posKeyPosKey(a, b=2, *args, d):
    print(a, b, args, d)
    
def 
