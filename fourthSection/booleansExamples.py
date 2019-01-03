''' Boolean is a subclass of int
    So all numbers besides 0 are TRUE in bool() form.
    This is because we are testing truthiness, and only
    0 is set to be false, all others assumed true.
'''

'''
type(True), id(True), int(True)
type(False), id(False), int(False)
None is False
(3 < 4) == True
(1 == 2) == False # True
1 == 2 == False # False
1 + True # = 2
100 * False # = 0
bool(0) # False
bool(1) # True
int(True) # 1
int(False) # 0
bool(100) # True
bool(-1) #True
'''

''' Every object has a true truth value, except:
    None
    False
    0 in any numeric type (0, 0.0 0+0j)
    empty sequences (list, tuple, string)
    empty mapping types (dictionary, set,...)
    custom classes that implement a __bool__ or __len__ method that returns False or 0
    '''

'''
# example: integers
def __bool__(self):
    return self != 0

so bool(100) executes 100.__bool__() and returns the result 100 != 0 which is True

with lists we can have:
    a = []
    which is a.__len__() # = 0
    thus,
    bool(a) # = False

bool(Fraction(0, 1)), bool(Decimal('0.0'))
False, False

a = []
b = ''
c = ()
False, False, False

a = {}
b = set()
false false

a = {'a': 1}
b = {1, 2}
True True

bool
'''

def two_null_examples(a):
    if a is not None and len(a) > 0:
        print(a[0])
    else:
        print('Nothing to see here...')
    if a:
        print(a[0])
    else:
        print('Nothing to see here...')

