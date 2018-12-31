''' Testing equalities!
'''
a = 10
b = a

a is b
# true

a == b
# true

###############################################

a = 'hello'
b = 'hello'

a is b
# should be true because strings are immutable
# therefore a and b are pointing to the same reference
# THIS IS NOT ALWAYS TRUE

a == b
# true, they have the same values

###############################################

a = [1, 2, 3]
b = [1, 2, 3]

a is b
# False because these are mutable objects 
# they will not reference the same location

a == b
# true, they have the same values

##################################################

a = 10
b = 10.0

a is b
# False since a shared reference won't be created

a == b
# TRUE!!!
