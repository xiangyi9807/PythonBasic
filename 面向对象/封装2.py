#! /usr/bin/env python
# author: vin

class Dog:
    def __init__(self, name, age):
        self.hidden_name = name
        self.hidden_age = age

    def sayHello(self):
        print('hello %s' % self.hidden_name)

    def get_name(self):
        return self.hidden_name

    def set_name(self, new_name):
        self.hidden_name = new_name

    def get_age(self):
        return self.hidden_age

    def set_age(self, new_age):
        if new_age > 0:
            self.hidden_age = new_age

d1 = Dog('alex', 3)
print(d1.get_name())
d1.sayHello()

d1.set_name('tom')
print(d1.get_name())
d1.sayHello()

d1.set_age(-1)
print(d1.get_age())