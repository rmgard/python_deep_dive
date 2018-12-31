import string, time

def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3

''' my_func.__code__.co_consts
    looks at all of the constants from the above function
    we get a lot of things namely:
    24 * 60 causes both '24,' and '60' to show up 
    as well as 1440
    (1, 2) shows up as the calculated (1, 2, 1, 2, ... , 2)
    You find 'ab' and '11' but not ab eleven times.
    'The quick brown fox will only show up a single time, and 
    the final list is a mutable object, not constant, so it won't
    be precalculated.
    '''

def my_func2(e):
    if e in [1, 2, 3]:
        pass

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass

def run_list():
    start = time.perf_counter()
    membership_test(10000000,char_list)
    end = time.perf_counter()
    print('list: ', end-start)

def run_tuple():
    start = time.perf_counter()
    membership_test(10000000,char_tuple)
    end = time.perf_counter()
    print('tuple: ', end-start)

def run_set():
    start = time.perf_counter()
    membership_test(10000000,char_set)
    end = time.perf_counter()
    print('set: ', end-start)
