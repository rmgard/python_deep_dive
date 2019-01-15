import random
''' The challenge is to randomize a
    list (shuffle the list)
    '''

l = [1,2,3,4,5,6,7,8,9]

def list_shuffle(l):
    ''' The following code takes a list, for each value it 
    randomly assigns a key to it and then sorts the value
    according to the randomized key.'''
    shuffle = sorted(l, key=lambda x: random.random())
    return shuffle
