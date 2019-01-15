class MyClass:
    def __init__(self, x=0):
        print('initializing...')
        self.counter = x

    def __call__(self, x=1):
        print('updating counter..')
        self.counter += x
