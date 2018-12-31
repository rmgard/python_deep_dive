import string

def basePrinter(i):
    base = 2
    while base < 37:
        try:
            print('{0} in base {1} is: {2}'.format(i, base, int(str(i), base)))
        except ValueError:
            print('Not a logical base {0} integer'.format(base))
        base += 1

# n = (n // b) * b + n % b
''' nBaseConvertor() was my attempt before watching
    all of the video for section 4 lecture 31.
    Once I saw the light, I rewrote this for iBaseRep()
    '''
def nBaseConvertor(i):
    base = 2
    print('{0} in base {1} is written: {2}'.format(i, 1, i))
    while base < 37:
        if base == 2:
            print('{0} in base {1} is written: {2}'.format(i, base, bin(i)))
        elif base == 8:
            print('{0} in base {1} is written: {2}'.format(i, base, oct(i)))
        elif base == 16:
            print('{0} in base {1} is written: {2}'.format(i, base, hex(i)))
        base += 1

def iBaseRep(n, b):
    if b < 2 or n < 0 : raise exception
    if n == 0: return [0]

    digits = []
    while n > 0:
        m = n % b
        n = n // b
        digits.insert(0, m)
    digit_map = '0123456789' + string.ascii_uppercase + string.ascii_lowercase
    if max(digits) >= len(digit_map):
        raise ValueError('digit_map is not long enough to encode the digits')
    encoding = ''
    for d in digits:
        encoding += digit_map[d]
    if b > 62:
        raise ValueError('Invalid base: cannot be > 62')
    sign = -1 if n < 0 else 1
    n *= sign
    if sign == -1:
        encoding = '-' + encoding
    return encoding
    
#####################################################################
# This is the teachers code
def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return[0]
    digits = []
    while n > 0:
        # m, n = n % b, n // b
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits

def encode(digits, digit_map):
    if max(digits) >= len(digit_map):
        raise ValueError('digit_map is not long enough to encode the digits')
    # encoding = ''
    # for d in digits:
    #     encoding += digit_map[d]
    # return encoding
    encoding = ''.join([digit_map[d] for d in digits])
    return encoding

def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding
