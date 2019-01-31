''' In order to have a value 'x' shared between two scopes:
    -outer
    -closure
    The label x is in two different scopes but always references the
    same value.
    Python does this by creating a cell as an intermediary object. (a cell)
    The cell points then to a string.
    '''
def outer():
    x = 'python'

    def inner():
        print('{0} rocks!'.format(x))

    # inner()
    return inner


#################################################
# Coding
#################################################
def outer2():
    x = [1, 2, 3]
    print(hex(id(x)))
    def inner():
        x = [1, 2, 3]
        print(hex(id(x)))
    return inner

''' The hashed comments through the next 10 lines
    are in reference to outer(), not outer2()...
    '''
fn2 = outer2()
# only one free variable exists
# ('x',)
fn_freevar = fn.__code__.co_frevars
# this shows us that the label points to a cell object
# and the cell object points to a string object
fn_closure = fn.__closure__


def outer_same():
    x = [1, 2, 3]
    print(hex(id(x)))
    def inner():
        y = x 
        print(hex(id(y)))
    return inner

######################################
def outer3():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

fn3 = outer3()
fn3_freevar = fn3.__code__.co_frevars
fn3_closure = fn3.__closure__

''' now let's add two incremental functions:
'''     
def outer4():
    count = 0

    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count +=
        return count
   # Return both closures 
    return inc1, inc2

fn4_1, fn4_2 = outer4()
fn4_1_freevar = fn4_1.__code__.co_frevars
fn4_2_freevar = fn4_2.__code__.co_frevars
''' if we keep calling fn4_1(), then it will
    increment, it will point to a different int,
    but the cell it points to as an intermediary
    will remain static.
    '''

def pow(n):
    def inner(x):
        return x ** n
    return inner

square = pow(2)
cube = pow(3)

################################
def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)
''' New cells are created for all functions.
    This makes sense because they are created with
    different closures.
    '''

adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)

''' These create lambdas, not closures.
    '''

def create_adders():
    adders = []
    for n in range(1,4):
        adders.append(lambda x: x + n)
    return adders

''' Now n points to the same n.
    So adders[0].__closure__
    and adders[1].__closure__
    point to the same cell
    '''

def create_adders2():
    adders = []
    for n in range(1,4):
        adders.append(lambda x, y=n: x + y)
    return adders
