''' How we might write a class as a closure
    instead
    '''

class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count

a = Averager()

''' We can write this class more simply:
    '''

def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total / count
    return add

a2 = averager()
b = averager

def averager2():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total = total + number 
        count = count + 1 
        return total / count
    return add

a3 = averager()
a3_clos = a3.__closure__
a3_freevar = a3.__code__.co_freevars

from time import perf_counter

class Timer:
    def __init__(self):
        self.start = perf_counter()

    # def poll(self):
    #    return perf_counter() - self.start

    def __call__(self):
        return perf_counter() - self.start

def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll
