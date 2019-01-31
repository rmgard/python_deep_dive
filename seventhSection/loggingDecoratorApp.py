def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(run_dt, fn.__name__))
        return result
    return inner

def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__, end-start))
        return result
    return inner

@logged
def func_1():
    pass

@logged 
def func_2():
    pass

''' The below is the same as:
    fact = logged(timed(fact))
    '''
@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))

def dec_1(fn):
    def inner():
        print('Running dec_1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print('Running dec_2')
        return fn()
    return inner

@dec_1
@dec_2
def my_func():
    print('running my_func')

def dec_3(fn):
    def inner():
        result = fn()
        print('Running dec_3')
        return result
    return inner

def dec_4(fn):
    def inner():
        result = fn()
        print('Running dec_4')
        return result
    return inner

@dec_3
@dec_4
def my_func2():
    print('running my_func2')

''' A security example might be
    @logged
    @auth
    def save_resource():
        pass
    
    This equates to 

    save_resource = logged(auth(save_resource))

    Thus, we log all attempts to save a resource
    even if the user isn't authorized to do so.
    '''

