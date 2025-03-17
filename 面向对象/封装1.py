#! /usr/bin/env python
# author: vin

class Dog:
    def __init__(self, name):
        self.hidden_name = name

    def sayHello(self):
        print('hello %s' % self.hidden_name)


d1 = Dog('tim')
d1.sayHello()

d1.name = 'tom'
d1.sayHello()