#! /usr/bin/env python
# author: vin

class Person(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def show(self):
        print(self.name)

if __name__ == '__main__':
    obj = Person('vin')
    obj.show()
    obj.setName('tom')
    print(obj.getName())
    obj.show()