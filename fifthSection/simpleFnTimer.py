import time

def time_it(fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep

# An example so we can see how time_it is handling args
def time_it_structure(fn, *args, rep=1, **kwargs):
    print(args, rep, kwargs)

''' We are going to write 3 versions of the 
    following 3 functions. 
    The first function will have parameters:
    we calculate powers of "n",
    then we have a start of "n^(start)"
    and an end of "n^(end)".
    The start and end are kwargs only,
    so we have * to stop positional args
    and we have start as an optional arg
    of start=1,
    and we have a nonoptional kwarg
    of end which is not set and therefore 
    forces our user to call and end arg.
    '''
def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results

def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return[n**i for i in range(start, end)]

def compute_powers_3(n, *, start=1, end):
    # using generators expression
    return(n**i for i in range(start, end))
