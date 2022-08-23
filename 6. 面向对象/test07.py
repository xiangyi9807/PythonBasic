#! /usr/bin/env python
# author: vin
'''
类方法
'''

class Person(object):
    def info(self):
        print('普通方法')

    @property
    def show(self):
         print('我是特性方法')


    @staticmethod
    def staticMethod():
        print('我是静态方法')

    @classmethod
    def classMethod(cls):
        print('我是类方法')

if __name__ == '__main__':
    obj = Person()
    obj.info()
    obj.show
    obj.staticMethod()
    Person.staticMethod()
    Person.classMethod()