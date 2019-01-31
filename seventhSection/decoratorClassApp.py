def my_dec(a, b):
    def dec(fn):
        def inner(*args, **kwargs):
            print('decorated function called: a={0}, b={1}'.format(a, b))
            return fn(*args, **kwargs)
        return inner
    return dec

@my_dec(10, 20)
def my_func(s):
    print('Hello {0}'.format(s))
    
my_func('World')

class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, c):
        print("called a={0}, b={1}, c={2}".format(self.a, self.b, c))

obj = MyClass(10,20)

class MyClass2:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print('decorated function called: a={0}, b={1}'.format(self.a, self.b))
            return fn(*args, **kwargs)
        return inner

@MyClass2(10, 20)
def my_func2(s):
    print('Hello {0}'.format(s))

obj = MyClass2(10,20)

def my_func3(s):
    print('Hello {0}'.format(s))

my_func3 = obj(my_func3)

