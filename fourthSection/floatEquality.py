''' Floating point numbers are not always exact, so we need them to be within
    some epsilon value:
    for some eps > 0, a = b iff |a - b| < eps
    COOL
    '''
import math

# fabs() is floating point absolute value in math module
def is_equal(x, y, eps):
    return math.fabs(x-y) < eps

x = 0.1 + 0.1 + 0.1
y = 0.3
a = 10000.1 + 10000.1 + 10000.1
b = 30000.3
abs_tol = 1e-15

''' |x - y| = 5.551115123125783e-17
    |a - b| = 3.637978807091713e-12
    Obviously if we use absolute tolerances,
    an epsilon value spec'd for x and y might 
    not work for an epsilon value spec'd for a and b.
    To see this in action, test is_equal() with
    abs_tol for both x, y pair and a,b pair
    '''
########################################################

''' For relative tolerance we want to look at a relative 
    percentage of the larger magnitude
    '''

# 0.001% = 0.00001 = 1e-5
rel_tol = 1e-5

# My function
def is_equal_rel(x, y, eps):
    if x > y:
        val = math.fabs(x-y) < x * rel_tol
    else:
        val = math.fabs(x-y) < y * rel_tol
    return val

''' tol = rel_tol * max(|x|, |y|)
'''

# Second function
def second_try(x, y, rel):
    tol = rel * max(math.fabs(x), math.fabs(y))
    val = is_equal(x,y, tol)
    return val

#######################################################
''' Using relative tolerances does not work very well
    near 0
    The math module has something that does this called:
    math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)
    round(x, ...) is more of an absolute version of isclose()
    '''

def near_zero(x, y, abs_tol, rel_tol):
    tol = max(rel_tol * max(math.fabs(x), math.fabs(y)), abs_tol)
    val = is_equal(x, y, tol)
    return val
