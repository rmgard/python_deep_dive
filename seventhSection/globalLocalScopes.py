######################################################################
# From the lecture, I went through some stuff on scopes
######################################################################
a = 10
def f1():
    print(a)

def f2():
    a = 100

def f3():
    global a
    a = 100

def f4():
    print(a)
    a = 100
    
######################################################################
# Start the coding section
######################################################################
def my_func(n):
    c = n ** 2
    return c

def my_func2(n):
    print('global a: ', a)
    c = a ** n
    return c

''' The a in the func below looks locally, not globally
    '''
def my_func3(n):
    a = 20
    c = a ** n
    return c

def my_func4(n):
    global a
    a = 20
    c = a ** n
    return c

''' local scope C global scope C built in scope'''
