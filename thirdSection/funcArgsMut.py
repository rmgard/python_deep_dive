def process(s):
    print('Initial s # = {0}'.format(id(s)))
    s = s + ' world'
    print('Final s # = {0}'.format(id(s)))

def modify_list(lst):
    print('Initial lst # = {0}'.format(id(lst)))
    lst.append(100)
    print('Final lst # = {0}'.format(id(lst)))

def modify_tuple(t):
    print('Initial t # = {0}'.format(id(t)))
    t[0].append(100)
    print('Final t # = {0}'.format(id(t)))

    
