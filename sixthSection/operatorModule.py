import operator
# See what's in the operator package
dir(operator)

from functools import reduce
l = [1,2,3,4]
times_list = reduce(lambda x, y: x*y, l)
op_times = reduce(operator.mul, l)

my_list = [1, 2, 3, 4]
''' Writing:
    operator.setitem(my_list, 1, 100)
    We then place 100 into the index = 1 slot,
    thus, 2 is replaced with 100 in my_list returning:
    [1, 100, 3, 4]
    '''

''' operator.delitem() can delete the indexed
    area
    '''
# setting f to itemgetter() will cause f to be a function 
# returning the 2 indexed item (third)
f = operator.itemgetter(2)

# attribute getters:
''' So first we create a basic class.
    Setting prop_a to attrgetter(), we can use the operator
    module to find obj.a
    '''
class MyClass:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30

    def test(self):
        print('test method running...')

obj = MyClass()
prop_a = operator.attrgetter('a')
print(prop_a(obj))
my_var = 'b'
''' This won't work!
    print(obj.my_var)
    '''
''' We can also add multiple attributes to be gotten: 
    Here is an example
    The below code will return 10 when you call 'a'
    20 when you call 'b'
    and 'test method running...' when you call 'test()'
    but not when you call 'test'
    '''

a, b, test = operator.attrgetter('a', 'b', 'test')(obj)

''' We can also use itemgetter() with sorting
    We will look at lambda examples vs operator examples:
    The below variables after lst will sort lst based
    on the first value in each element of lst
    '''
lst = [(2, 3, 4), (1, 3, 5), (6,), (4, 100)]
lamb_sort = sorted(lst, key=lambda x: x[0])
op_sort = sorted(lst, key=operator.itemgetter(0))

''' Let's look at methodcaller(). We can use a convoluted
    syntax to call the test() method in MyClass, or 
    we can use methodcaller()
    '''

att_f = operator.attrgetter('test')
att_f(obj) # returns a info about test()
att_f(obj)() # returns 'test method running...'

meth_call_f = operator.methodcaller('test')
meth_call_f(obj)

''' methodcaller() can handle extra attributes as well:
    '''

class MyClass2:
    def __init__(self):
        self.a = 10
        self.b = 20

    def test(self, c):
        print(self.a, self.b, c)

obj2 = MyClass2()
''' Now:
    obj2.a = 10
    obj2.b = 20
    obj.test(100) = 10 20 100
    '''

method_caller2 = operator.methodcaller('test', 100)(obj2)
