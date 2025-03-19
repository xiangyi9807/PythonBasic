#! /usr/bin/env python
# author: vin

class A():
    def __init__(self):
        self.name = 'A类'

    # __del__是特殊方法，对象被垃圾回收前调用
    def __del__(self):
        print('垃圾回收前调用', self)


a = A()
# del a
a = None