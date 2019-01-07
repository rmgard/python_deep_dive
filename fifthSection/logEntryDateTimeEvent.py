from datetime import datetime

''' arg "dt" gets created when called.
    Therefore, no new "dt" will be created
    once log() is called again.
    '''
def log(msg, *, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))

# Solution: set dt to None
def log2(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    # if not dt:
    #   dt = datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))

