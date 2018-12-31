''' if we make a var called "my_var = 10" then we basically have this thing called my_var that is
    pointing to an integer "10" stored in a location. The teacher calls the location
    arbitrarilly "0x1000".
    '''

my_var = 10

'''Now... if we reference the location of "my_var" then we can count the reference. The
    counter will count 1 reference for 0x1000. If we say other_var = my_var,
    then the reference counter will tick up to 2. my_var and other_var are stored in the 
    same location.
    '''

other_var = my_var

#################################################################################

import sys

a = [1, 2, 3]

a_id = id(a) # the memory address which a points to (a is a pointer)

a_refid = sys.getrefcount(a) # This counts the number of references

import ctypes

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value



