def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner

def add(a, b):
    return a + b

def mult(a, b):
    return a * b

counter_add = counter(add)
''' We have two free vars here: 'cnt' and 'fn'
    2 cells are pointed to which point to an int (cnt)
    and a function object (fn)
    '''

result = counter_add(10,20)
counter_mult = counter(mult)

######################################
counters = dict()
def counter2(fn, counters):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

def fact(n):
    product = 1
    for i in range(2, n+1):
        product *= i
    return product

''' we can say:
    fact = counter(fact, c)
    then fact.__closure__ points to three cells
    fact() turns into the fact var
    '''

