#! /usr/bin/env python
# author: vin

class Person():
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def sayHello(self):
        print('hello %s' % self.__name)

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

p1 = Person('vin', 20)
p1.sayHello()
p1.set_name('tom')
p1.sayHello()
# print(p1.__name)  报错