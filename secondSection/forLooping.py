############################################################
''' traditionally for loops might be written:
    c style languages
    for (int i = 0; i < 5; i++) { ... }
    '''
# In Python, an iterable is an object capable of returning values one at a time.

def while_loop():
    i = 0
    while i < 5:
        print(i)
        i += 1
        i = None

def for_loop():
    for a in range(5):
        print(a)

def for_list():
    for i in [1, 2, 3, 4]:
        print(i)

def for_string():
    for c in 'hello':
        print(c)

def for_tuple():
    for x in ('a', 'b', 'c', 4):
        print(x)

def for_tuple_individual_extraction():
    for i, j in [(1, 2), (3, 4), (5, 6)]:
        print(i, j)
