''' numbers in python are immutable
    Strings are immutable
    Tuples are immutable
    Frozen Sets
    User-defined classes

    Mutable:
    lists
    sets
    dictionaries
    user-defined classes
    '''
# Tuples are immutable: 
# elements cannot be deleted, inserted, or replaced
# in the below case, both the container (tuple), 
# and all its elements (ints) are immutable
t = (1, 2, 3)

#Consider
a = [1, 2]
b = [3, 4]
t = (a, b)

a.append(3)
b.append(5)

#############################################################

my_list = [1,2,3]

type(my_list)
id(my_list)
my_list.append(4)

# Immutability does not mean frozen!!!!!!!!!!!!!!!!!!!!!!!!!
