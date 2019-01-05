a, b, *c = 10, 20, 'a', 'b', 'c'

def func1(a, b, *args):
    print(a)
    print(b)
    print(args)

# My average function...
def my_avg(*args):
    count = len(args)
    total = sum(args)
    try:
        mu = total/count
    except ZeroDivisionError:
        mu = 'You are finding the average of nothing!'
    return mu

# lecturer's first function
def teach_avg(*args):
    count = len(args)
    total = sum(args)
    if count == 0:
        return 0
    else:
        return total/count

# Blast... that's good.
def conditional_avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count

def req_avg(a, *args):
    count = len(args) + 1
    total = sum(args) + a
    return total/count:w

def func2(a, b, c):
    print(a)
    print(b)
    print(c)

''' To use this, we can't put:
    l = [10, 20, 30]
    we must do func2(*l) to unpack it first.
