'''
    not(A or B) == not(A) and (not B)
    not(A and B) == not(A) or (not B)
    not(x < y) == x >= y
    not(x <= y) == x > y

    Operator Precedence:
    ()
    < > <= >= == != in is
    not
    and
    or
    '''
''' Short circuiting:
    If we have X or Y, and X is True, then Y does not need to be calculated
    If we have X and Y, and X is False, then Y does not need to be calculated.
    '''
# Some sudo code
if symbol in watch_list:
    if price(symbol) > threshold:
        # do something

if symbol in watch_list and price(symbol) > threshold:
    # do something

if name[0] in string.digits:
    # do something
    # This code breaks if name is None or an empty string

if name and name[0] in string.digits:
    # do something
    # if name is falsy (None or empty string) then name[0] in string.digits is NOT evaluated

a = 10
b = 2

if b > 0 and  a/b > 2:
    print('a is at least twice b')

    # same as
if b and a/b > 2:
    print('a is at least twice b'

name = 'Bob'
if name > 0 and name[0] in string.digits:
    print('Name cannot start with a digit.')

###################################################################################

s1 = None
s2 = ''
s3 = 'abc'

print(s1 and s1[0])
print(s2 and s2[0])
print(s3 and s3[0])

print((s1 and s1[0]) or '')
print((s2 and s2[0]) or '')
print((s3 and s3[0]) or '')
