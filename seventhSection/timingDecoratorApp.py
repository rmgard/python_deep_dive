def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end - start

        args_ = [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args) #comma delimited representation

        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__,
                                                      args_str, 
                                                      elapsed))
        return result
    return inner

''' three methods to calculate the fib numbers:
    1. recursion
    2. loop
    3. reduce
    '''

def calc_recursive_fib(n):
    if n <= 2: 
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)

@timed
def fib_recursive(n):
    return calc_recursive_fib(n)

@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

''' n = 1
    (1,0) --> (1, 1) result t[0] = 1

    n = 2
    (1, 0) --> (1, 1) --> (2, 1) result t[0] = 2

    n = 3
    (1, 0) --> (1, 1) --> (2, 1) --> (3, 2) result t[0] = 3

    n = 4
    (1, 0) --> (1, 1) --> (2, 1) --> (3, 2) --> (4, 3) result t[0] = 5
    '''

from functools import reduce

@timed
def fib_reduce(n):
    initial = (1, 0)
    dummy = range(n-1)
    fib_n = reduce(lambda prev, n: (prev[0] + prev[1], prev[0]), 
                   dummy, 
                   initial)
    return fib_n[0]
