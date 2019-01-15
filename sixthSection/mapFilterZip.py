def fact(n):
    return 1 if n < 2 else n * fact(n-1)

results = map(fact, range(6))
results_list = list(map(fact, range(6)))

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
l3 = 100, 200, 300, 400
results2 = list(map(lambda x, y: x+y, l1, l2))
results3 = list(map(lambda x, y: x+y+z, l1, l2, l3))

''' Range, unlike map and filter can be reused
    Looking at filters:
    '''

x = range(25)

list(filter(lambda x: x % 3 == 0, range(25)))
rnd_filter = filter(None, [1, 2, 4, 'a', '', None, True, False]))


l4 = [1, 2, 3, 4]
l5 = [10, 20, 30, 40]
l6 = 'python' 
rslts = list(zip(l4, l5, l6))
