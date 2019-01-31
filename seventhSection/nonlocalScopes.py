''' nonlocal works similarly to 'global'
    when looking at a function into the module
    '''
def outer():
    x = 'hello'

    def inner1():
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        print('inner(before)', x)
        inner2()
        print('inner(after)', x)

    inner1()
    print('outer', x)

''' Similarly to the func above,
    we add a global aspect to our inner funcs
    ''' 
x = 100
def outer2():
    x = 'python'

    def inner1():
        nonlocal x
        x = 'monty'
        def inner2():
            global x
            x = 'hello'
        print('inner(before)', x)
        inner2()
        print('inner(after)', x)

    inner1()
    print('outer2', x)
outer2()
print(x)

#############################################################
# Coding section
#############################################################
def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
    inner_func()

def outer_func2():
    x = 'hello'
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()
    
def outer_func3():
    x = 'hello'
    def inner():
        x = 'python'
        print('inner: ', x)
    inner()
    print('outer: ', x)
    
def outer_func4():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
        print('inner: ', x)
    print('outer(before): ', x)
    inner()
    print('outer(after): ', x)

def outer_func5():
    x = 'hello'
    def inner1():
        def inner2():
            nonlocal x
            x = 'python'
        inner2()
    inner1()
    print(x)

def outer_func6():
    x = 'hello'
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        inner2()
    inner1()
    print(x)

def outer_func7():
    global x
    x = 'monty'

    def inner():
        nonlocal x
        x = 'hello'
    inner()
    print(x)
