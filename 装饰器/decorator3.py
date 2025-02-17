# -*- coding:utf-8 -*-
# xy

import time


def timmer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        stop_time = time.time()
        print('the func run time is %s' % (stop_time - start_time))
    return wrapper


@timmer
def test1():
    time.sleep(1)
    print('in the test1')


@timmer
def test2(name):
    print("test2:", name)


test1()
test2('vin')