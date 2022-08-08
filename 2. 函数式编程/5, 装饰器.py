import time


def decorater(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print(stop_time - start_time)
    return wrapper

@decorater
def info():
    print('hello world')

info()