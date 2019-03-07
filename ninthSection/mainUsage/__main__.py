# __main__.py

'''
print(f'loading __main__.py: __name__ = {__name__}')

import module1
'''

import timing

code = '[x**2 for x in range(1_000)]'

result = timing.timeit(code, 100)
print(result)