s = [1, 2, 3]

print(len(s))

from math import sqrt

print(sqrt(4))

import math

def func_1():
    print('running func_1')

''' putting in 'int' is just for readability and does not cause inputs to be
explicitly an 'int'''

def func_2(a: int, b: int):
    return a * b

#############################################################

def func_3():
    return func_4()

def func_4():
    return 'running function 4'

# This is broken because func_6 is not defined yet.
def func_5():
    return func_6()

############################################################
# LAMBDAS!
############################################################

my_func = func_4

lambda x: x**2

fn1 = lambda x: x**2
