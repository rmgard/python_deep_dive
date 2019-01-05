#######################################################
# Unpacking
#######################################################

def trad_unpack(a, b):
    tmp = a
    a = b
    b = tmp
    print('a was {0}, but is now {1}. b was {1}, but is now {0}'.format(b, a))

def py_unpack(a, b):
    a, b = b, a
    print('a was {0}, but is now {1}. b was {1}, but is now {0}'.format(b, a))

########################################################
''' sets and dictionaries are unordered types, so setting 
    variables can be more complicated.'''

# Unpack lists into tuples
########################################################
''' sets and dictionaries are unordered types, so setting 
    variables can be more complicated.'''

o = (1, 2, 3)

a, b, c = [1, 'a', 3.14]
e, f, g = o
d = {'key1': 1234, 'key2': 5678, 'key3': 9101, 'key4': 1121, 'key5': 3141}

def iterable_unpack(i):
    for e in i:
        print(e)
        
# so the above function will print out the keys, below prints the values.
def dict_value_unpack(d):
    for e in d.values():
        print(e)
        
# Now let's look at a function to unpack the keys and values

def functional_unpack_of_items(d):
    for e in d.items():
        a, b = e
        print('key: {0}, value: {1}'.format(a,b))
        
def for_loop_unpack_of_items(d):
    for a, b in d.items():
        print('key: {0}, value: {1}'.format(a,b))

#########################################################
# * **
#########################################################

# Two ways to slice and unpack

l = [1,2,3,4,5,6]

# below only works for iterables.
def list_index(l):
    a = l[0]
    b = l[1:]
    print(a, b)

def star_unpack(l):
    a, *b = l
    print(a, b)

s = 'python'
t = ('a', 'b', 'c')
s1 = 'abc'
s2 = 'cde'

# sets will remove repetitions:
def sets_and_lists(a, b):
    y = [*a, *b]
    z = {*a, *b}
    print('list: {0}, set: {1}'.format(y,z))

# union and *
set1 = {1,2,3}
set2 = {3,4,5}
set3 = {5,6,7}
set4 = {7,8,9}

def union_and_star(a,b,c,d):
    unionunion = set1.union(set2).union(set3).union(set4)
    union = set1.union(set2, set3, set4)
    star = {*set1, *set2, *set3, *set4}
    print('multiple unions:{0}, one union: {1}, star function: {2}'.format(unionunion, union, star))
