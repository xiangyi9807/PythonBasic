#! /usr/bin/env python
# author: vin

class Person(object):
    '''
    内置类演示
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        pass

    def __call__(self, *args, **kwargs):
        self.show()

    def show(self):
        print('姓名:{0}，年龄：{1}'.format(self.name, self.age))

    def __str__(self):
        return '姓名:{0}，年龄：{1}'.format(self.name, self.age)

if __name__ == '__main__':
    obj = Person('vin', 20)
    print(obj())
    print(obj.__doc__)
    print(obj.__call__)