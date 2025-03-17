#! /usr/bin/env python
# author: vin

class Animal():
    def run(self):
        print('Animal running~~')

    def sleep(self):
        print('Animal sleeping~~')


class Dog(Animal):
    def run(self):
        print('Dog running~~')

    def bark(self):
        print('Dog barking~~')


d = Dog()
d.run()
d.sleep()
d.bark()

print(isinstance(d, Animal))
print(isinstance(d, Dog))

print(isinstance(print, object))

print(issubclass(Dog, Animal))
