import sys
import time

def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)
    for i in range(n):
        if a is b:
            pass

def run_equals():
    start = time.perf_counter()
    compare_using_equals(10000000)
    end = time.perf_counter()
    print('equality', end-start)

def run_interning():
    start = time.perf_counter()
    compare_using_interning(10000000)
    end = time.perf_counter()
    print('equality', end-start)
