import decimal
from decimal import Decimal
import math
import time

'''
GLOBAL CONTEXT
gctx = decimal.getcontext()

gctx.prec = 6
gctx.rounding = decimal.ROUND_HALF_UP

gctx.prec = 28
gctx.rounding = decimal.ROUND_HALF_EVEN
'''

''' decimal.localcontext()

    with decimal.localcontext() as ctx:
        print(type(ctx))
        print(ctx)
        ctx.prec = 6
        ctx.rounding = decimal.ROUND_HALF_UP
    '''

x = Decimal('1.25')
y = Decimal('1.35')

# Inside the with we are in a local context, outside we are in a global
def glob_v_loc_context(x, y):
    with decimal.localcontext() as ctx:
        ctx.prec = 6
        ctx.rounding = decimal.ROUND_HALF_UP
        print(round(x, 1))
        print(round(y, 1))
    print(round(x, 1))
    print(round(y, 1))

# tuple example:
a = Decimal((1, (3, 1, 4, 1, 5), -4)) # a -> -3.1415
# 1 marks a negative, followed by the number, followed by x10^-4

# n = d * (n // d) + (n % d)
# for decimals a // b = trunc(a/b) causing issues with negatives for instance

def dec_v_float(x, y):
    a = x//y
    b = x%y
    c = divmod(x, y)
    dec_x = Decimal(x)
    dec_y = Decimal(y)
    d = dec_x//dec_y
    f = dec_x%dec_y
    g = divmod(dec_x, dec_y)
    print(a, b, c, d, f, g)
    print(x == y * (x//y) + (x%y))
    print(dec_x == dec_y * (dec_x//dec_y) + (dec_x%dec_y))

def float_v_mixed_root(x, x_dec):
    root_float = math.sqrt(x)
    root_mixed = math.sqrt(x_dec)
    root_dec = x_dec.sqrt()
    print(format(root_float, '1.27f'))
    print(format(root_mixed, '1.27f'))
    print(root_dec)
    print(format(root_float * root_float, '1.27f'))
    print(format(root_mixed * root_mixed, '1.27f'))
    print(root_dec * root_dec)

def run_float(n=1):
    for i in range(n):
        a = 3.1415
    
def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')

def run_float_add(n=1):
    a = 3.1415
    for i in range(n):
        a + a
    
def run_decimal_add(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a

def timer_float_dec(n=10000000, mod = 0):
    start = time.perf_counter()
    if mod == 0:
        run_float(n)
    elif mod == 1:
        run_decimal(n)
    elif mod == 2:
        run_float_add(n)
    else:
        run_decimal_add(n)
    end = time.perf_counter()
    if mod == 0:
        print('float: ', end - start)
    elif mod == 1:
        print('decimal: ', end - start)
    elif mod == 2:
        print('floats added: ', end - start)
    else:
        print('decimals added: ', end - start)

