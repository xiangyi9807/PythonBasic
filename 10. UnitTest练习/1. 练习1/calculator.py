#! /usr/bin/env python
# author: vin

'''带测试程序'''

class Count(object):

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.b - self.a
