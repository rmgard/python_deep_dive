def add_item(name, quantity, unit, grocery_list):
    grocery_list.append('{0} ({1} {2})'.format(name, quantity, unit))
    return grocery_list

store1 = []
store2 = []

def add_item2(name, quantity, unit, grocery_list=[]):
    grocery_list.append('{0} ({1} {2})'.format(name, quantity, unit))
    return grocery_list

def add_item3(name, quantity, unit, grocery_list=None):
    grocery_list = grocery_list or []
    # if not grocery_list:
    #   grocery_list = []
    grocery_list.append('{0} ({1} {2})'.format(name, quantity, unit))
    return grocery_list

###############################

def factorial(n):
    if n < 1: 
        return 1
    else:
        print('calculating{0}!'.format(n))
        return n * factorial(n-1)

cache = {}
def factorial2(n, *, cache):
    if n < 1: 
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating{0}!'.format(n))
        result = n * factorial2(n-1, cache=cache)
        cache[n] = result
        return result

