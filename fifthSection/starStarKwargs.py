''' **kwargs:
    with **kwargs (key word arguments) we can pass a variety
    of key words into a function, and they will all be scooped
    up and placed into a dictionary.'''
def star_star_kwargs(**other):
    print(others)

''' The below example moves from positional to
    keyword arguments.'''
def args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

''' The broken example below will not work, returning the error:
    SyntaxError: named arguments must follow bare *
    This is because the star says "no more positional arguments,"
    so kwargs is kind of redundant.
    The fixed function works because we have an explicitly 
    needed keyword argument in "d"
    '''
    
'''def broken_star_kwarg(a, b, *, **kwargs):
    print(a)
    print(b)
    print(kwargs)
    '''

def fixed_star_kwargs(a, b, *, d, **kwargs):
    print(a)
    print(b)
    print(d)
    print(kwargs)
