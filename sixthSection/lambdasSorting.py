''' If we look below we and we
    run the first sorted, then we will end up with
    ['B', 'D', 'a', 'c']
    This happens because the characters are ordered 
    off of their ord() placement.
    For instance ord('a') = 97
    and ord('A') = 65
    With the lambda example, we basically take the upper case
    values of each character, so that we get them ordered
    alphabetically regardless of case.
    '''
l = ['c', 'B', 'D', 'a']
def sort_and_lambdasort(l):
    sort = sorted(l)
    lam_sort = sorted(l, key = lambda s: s.upper())
    return (sort, lam_sort)

''' Now let's look at dictionaries
    '''
d = {'abc': 200, 'def': 300, 'ghi': 100}

def dict_sort_example(d):
    ''' In this example, we can use sorted() 
    to sort by the key values of the dictionary,
    or we can use the lambda function to retrieve
    the actual values of the dictionary.
    '''
    for e in d:
        print(e)
    sort = sorted(d)
    lam_sort = sorted(d, key = lambda e: d[e])
    return (sort, lam_sort)

def dist_sq(x):
    return (x.real)**2 + (x.imag)**2
'''
sorted(l, key=dist_sq)

sorted(l, key=lambda x: (x.real)**2 + (x.imag)**2

monty = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
sorted(monty)
sorted(l, key=lambda s: s[-1])
'''
