''' What if we only want to parameters in my_func()?
    See how fn() uses my_func, but presets the value of a?
    '''
def my_func(a, b, c):
    print(a, b, c)

def fn(b, c):
    return my_func(10, b, c)

''' We can also use functools.partial
    With partial() you define the vars you don't want to 
    feed into the function.
    '''
from functools import partial
f = partial(my_func, 10)
# We can do the same thing using a lambda
lambda_f = lambda x, y: my_func(x, y)

''' We can also handle more complex arguments
    '''
def my_complex_func(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

def complex_f(b, *args, k2, **kwargs):
    return my_complex_func(10, b, *args, k1='a', k2=k2, **kwargs)

complex_f = partial(my_complex_func, 10, k1='a')

''' Handling complex arguments such as power:
    '''
def pow(base, exponent):
    return base ** exponent

square = partial(pow, exponent=2)
cube = partial(pow, exponent=3)

#############################################################
# Using mutable types.... Let's look at a list
#############################################################
def mutable_func(a, b):
    print(a, b)

a = [1, 2]
mutable_f = partial(my_func, a)

#############################################################
# Sorting with partials
#############################################################
origin = (0, 0)
points = [(1, 1), (0, 2), (-3, 2), (0, 0), (10, 10)]

dist2 = lambda a, b: (a[0] - b[0])**2 + (a[1] - b[1])**2
net_dist = partial(dist2, origin)
basic_sort = sorted(points)
key_sort = sorted(points, key=net_dist)
