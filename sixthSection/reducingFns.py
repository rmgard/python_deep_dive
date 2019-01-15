l = [5, 8, 6, 20, 9]

max_value = lambda a, b: a if a > b else b

def max_sequence(sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = max_value(result, e)
    return result

##################################
# Min example
##################################
min_value = lambda a, b: a if a < b else b

def min_sequence(sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = min_value(result, e)
    return result

###################################
# Reduce fn that is more generalized!
####################################
def _reduce(fn, sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = fn(result, e)
    return result

'''If we pipe the bellow add fn into reduce(),
then we basically end up with the sum() fn
'''

add = lambda a, b: a+b

##########################################
# Now python's reduce!
##########################################
from functools import reduce
py_max = reduce(max_value, l)
py_min = reduce(min_value, l)
py_sum = reduce(add, l)
py_awe = reduce(lambda a, b: a + ' ' + b, ('python', 'is', 'awesome!'))

#########################################
# any and all
########################################
''' any:
    True if any element in l is truthy
    False otherwise

    all:
    True if every element in l is truthy
    False otherwise

    Below we show an example of what any is doing:
'''

lst = [0, '', None, 100]

# big any fn
lst_result = bool(0) or bool('') or bool(None) or bool(100)
lst_result2 = reduce(lambda a, b: bool(a) or bool(b), lst)

lst_all = bool(0) and bool('') and bool(None) and bool(100)
lst_all2 = reduce(lambda a, b: bool(a) and bool(b), lst)

###########################################
# Product
######################################
py_prod = reduce(lambda a, b: a * b, l)

''' Some built in reduce functions are
    min, max, sum, all, and any
    '''

s = {True, 1, 0, None}
# any(s) = True
# all(s) = False

###################################################3
# Reduce with initializer for empty sets
###################################################

def _reduce2(fn, seq, initial):
    result = initial
    for x in seq:
        result = fn(result, x)
    return result
