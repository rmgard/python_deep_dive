''' We have a few methods to go from float to int:
    truncation
    floor
    ceiling
    rounding
    '''

import math

# int() uses truncation to turn floats to ints

# floor: floor(x) = max{i in Z | i <= x}

# ceiling: ceil(x) = min{i in Z | i >= x}

from math import trunc

a, b, c = trunc(-10.3), trunc(-10.5), trunc(-10.9)

from math import floor
x, y, z = floor(-10.3), floor(-10.5), floor(-10.9)
from math import ceil
u, v, w = ceil(-10.3), ceil(-10.5), ceil(-10.9)

##########################################################
# ROUNDING
##########################################################

x = 1.25
# round(x, 1) = 1.2
''' IEEE 754 standard: rounds to the nearest value,
    with ties rounded to the nearest value with an even
    least significant digit
    '''
    
''' Why banker's rounding?
    less biased than ties away from zero
    consider averaging:
    0.5, 1.5, 2.5
    mu = 4.5/3 = 1.5
    STANDARD ROUNDING:
    mu_std = (1 + 2 + 3)/3 = 6/3 = 2
    BANKER'S ROUNDING:
    mu_bnk = (0 + 2 + 2)/3 = 1.333333...
    '''
    
''' How to correctly round away from zero:
    sign(x) * int(abs(x)+0.5)
    '''

# sign(x) can be gotten using math.copysign(). Below I use numpy.sign()
import numpy as np
def round_from_zero(x):
    return np.sign(x) * int(abs(x)+0.5)

# The teacher's function:
def round_up(x):
    from math import fabs, copysign
    return copysign(1,x) * int(fabs(x) + 0.5)

# Or a simpler way is:
def _round(x):
    from math import copysign
    return int(x + copysign(1, x))
