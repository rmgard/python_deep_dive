 # n = d * (n // d) + (n % d) 
  #  n is numerator
  #  d is denomenator
  #  '''

n = 155
d = 4

''' The floor of a real number a is the largest int <= a
    floor(3.14) = 3
    floor(1.9999999) = 1
    floor(2) = 2
    floor(-3.1) = -4
    '''

''' a = 13
    b = 4
    13 / 4 = 3.25
    13 // 4 = 3
    13 % 4 = 1
    '''

''' a = -13
    b = 4
    -13 / 4 = -3.25
    -13 // 4 = -4
    -13 % 4 = 3
    '''

''' a = 13
    b = -4
    13 / -4 = -3.25
    13 // -4 = -4
    13 % -4 = -3
    '''

''' a = -13
    b = -4
    -13 / -4 = 3.25
    -13 // -4 = 3
    -13 % -4 = -1
    '''

def std_division(a, b):
    print('{0}/{1} = {2}'.format(a, b, a/b))

def std_div(a, b):
    print('{0}//{1} = {2}'.format(a, b, a//b))

def std_mod(a, b):
    print('{0}%{1} = {2}'.format(a, b, a%b))

def lesson_equation(a,b):
    std_division(a,b)
    std_div(a,b)
    std_mod(a,b)
    print(a == b * (a//b) + (a%b))
