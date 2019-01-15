from inspect import isfunction, ismethod, isroutine
import inspect

''' function and method:
    classes and objects have attributes - an object that is bound to the class/object
    an attribute that is callable is called a method
    examples:
    '''

def my_func(a, b=2, c=3, * kw1, kw2=2):
    ''' This function is not bound as an attribute, so it's a FUNCTION.
    '''
    pass

def MyClass():
    ''' func() below is an instance function/ instance METHOD. 
    An attribute bound to MyClass
    '''
    def func(self):
        pass

my_obj = MyClass()

##################################################################
# Looking at callable sigs
##################################################################

def callable_sigs(a: 'a string',
                  b: int = 1,
                  *args: 'additional positional args',
                  kw1: 'first keyword-only arg',
                  kw2: 'second keyword-only arg' = 10,
                  **kwargs: 'additional keyword-only args') -> 'does nothing':
    ''' does nothing
        or other'''
    i = 10
    j = 20

def inspect_callables(fn):
    for param in inspect.signature(fn).parameters.values():
        print('Name:', param.name)
        print('Default: ', param.default)
        print('Annotation: ', param.annotation)
        print('Kind: ', param.kind)
        print('-----------------------')

# TODO: this is a todo 
# currently does nothing:w
# inspect.getcomments(fn)
def func_call(f):
    print(id(f))
    print(f.__name__)
