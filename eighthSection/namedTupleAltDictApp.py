data_dict = dict(key1=100, key2=200, key3=300)

# we're better off using namedtuple than the above

from collections import namedtuple

# Data = namedtuple('Data', 'key1 key2 key3')
# python 3.6 and above, order is guaranteed
Data = namedtuple('Data', datadict.keys())

data_list = [
        {'key1': 2, 'key2': 1},
        {'key1': 3, 'key2': 4},
        {'key1': 5, 'key2': 6, 'key3': 7},
        {'key2': 100}
        ]

keys = {key for dict_ in data_list for key in dict_.keys()}

keys

Struct = namedtuple('Struct', sorted(keys))

tuple_list = []

for dict_ in data_list:
    tuple_list.append(Struct(**dict_))
print(tuple_list)

def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', keys)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]

tuple_list = tuplify_dicts(data_list)

tuple_list
