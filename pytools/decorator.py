import time


"""
how to generate a decorator
example that measures time or print stuff
"""

def timeit(function):

    def wrapper(*args, **kwargs):
        start = time.time()
        ans = function(*args, **kwargs)
        end = time.time()
        print(f'elapsed time : {(end - start)*1000.:.0f}ms')
        return ans
    
    return wrapper


def calltime(function):

    def wrapper(*args, **kwargs):
        print(f'function called on {time.asctime()} with args {args}')
        ans = function(*args, **kwargs)
        return ans
    
    return wrapper


@calltime
@timeit
def fun(x):
    time.sleep(0.1 * x)
    return 2 * x


fun(2)
fun(3)
fun(4)
