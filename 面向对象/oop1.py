# -*- coding:utf-8 -*-
# xy

class Person(object):
    def __init__(self, name, age):
        self.age = age
        self.name = name

    def sayHi(self):
        print('hello %s' % self.name)


p1 = Person('vin', 25)
p1.sayHi()