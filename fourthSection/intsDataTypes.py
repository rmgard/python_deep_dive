import sys, time

def calc(a):
    for i in range(10000000):
        a * 2

def run_calc(n):
    start = time.perf_counter()
    calc(n)
    end = time.perf_counter()
    print(end - start)
