def my_func(a: 'a string', b: 'a positive integer') -> 'a string':
    return a * b

''' annotations can be any expression. 
    Sphinx can use these annotations
    my_func.__doc__ shows annotations 
    Below we will do a function with inside annotations
    and a docstring. These serve as metadata
    which offer code explanation when using help(my_func)
    Check PEP 3107 for details about annotations.
    '''

def my_func2(a: 'annotation for a',
             b: 'annotation for b' = 1) -> 'something with a long annotation':
    '''documentation for my_func2'''
    return a * b

def kwarg_func(a: str,
               b: 'int > 0' = 1,
               *args: 'some extra positional ars',
               k1: 'keyword-only arg 1',
               k2: 'keyword-only arg 2' = 100,
               **kwargs: 'some extra keyword-only args') -> 'something':
    print(a, b, args, k1, k2, kwargs)
