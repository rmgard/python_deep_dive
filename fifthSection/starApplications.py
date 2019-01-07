''' One example is the print() function.
    We can change the input arguments for print as such:
    '''

print(1, 2, 3)
print(4, 5, 6)
print(1, 2, 3, sep= '-', end = '*****')
print(4, 5, 6, sep='?')

''' often keyword arguments are used to change
    the way the function works.'''

def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = min(args) if len(args) > 0 else 0
#    if len(args) == 0:
#        lo = 0
#    else:
#        lo = min(args)
    avg = (hi + lo) / 2
    if log_to_console:
        print('high={0}, low={1}, avg={2}'.format(hi, lo, avg))
    return avg

''' Useful VIM:
    :%s!^!//! replaces the beginning of each line with "//"
    :'<,'>s!^!//! replaces the beginning of each selected 
    line selected with visual block mode with "//"
    '''
