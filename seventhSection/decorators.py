def counter(fn):
    count =0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__, count)) 
        return fn(*args, **kwargs)
    return inner

@counter
def add(a, b=0):
    return a + B

add = counter(add)
result = add(1, 2)

''' We modified our add function by wrapping
    it inside another function that added some functionality to it.

    We have decorated our function 'add' with the function 'counter'
    'counter' is a decorator funtion

    Decorators:
    In general a decorator function:
    - takes a function as an arg
    - returns a closure
    - the closure usally accepts any combo of parameters
    - runs some code in the inner function (closure)
    - closure ffn calls the og fn using the args passed to the closure
    - returns whatever is returned by that fn call

    @ symbol is a convenient decorator tool
    '''
################################################
@counter
def mult(a, b, c=1):
    ''' returns the product of three values
    '''
    return a * b * c

# mult.__name__ : is 'inner' not 'mult'

''' To fix our inability to reference the original
    function, we can try to fix this problem:
    '''

def counter2(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print('function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner

''' The functools.wraps function:
    functools module has a wraps function that we can
    use to fix the metadata of our inner function in
    our decorator
    In fact the wraps function is itself a decorator
    but it needs to know what was our 'original function - fn
    '''

from functools import wraps

def counter_convoluted_wraps(fn):
    count = 0
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return fn(*args, **kwargs)
    inner = wraps(fn)(inner)
    return inner

def counter_atsymbol_wraps(fn):
    count = 0
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count
        count += 1
        print(count)
        return fn(*args, **kwargs)
    return inner

