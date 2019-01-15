''' lambda [parameter list]: expression
    the entire expression returns a function object
    '''
lambda x: x**2
lambda x, y: x + y
lambda : 'hello'
lambda s: s[::-1].upper()
my_func = lambda x: x**2
''' type(my_func) -> function
    my_func(3) -> 9
    my_func(4) -> 16
    it's identical to:
    def my_func(x):
        return x**2
    '''

###############################################################
# Coding Section
###############################################################
def sq(x):
    ''' This is a standard function'''
    return x**2

# Now we can compare the regular function to a lambda
lam = lambda x: x**2

f = sq

# We can also set default values:
g = lambda x, y=10: x+y

# We can make lambda fns more complicated as well:
j = lambda x, *args, y, **kwargs: (x, args, y, kwargs)

# We can pass lambdas into standard functions:
def apply_func(x, fn):
    return fn(x)

# Here we can pass arbitrary numbers of args and kwargs:
def apply_func2(fn, *args, **kwargs):
    return fn(*args, **kwargs)
