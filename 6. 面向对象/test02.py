#! /usr/bin/env python
# author: vin

'''
类属性:属于类，但是也可以使用对象调用，结果是等价的，建议类调用
实例属性，属于对象，只能使用对象调用
'''

class Person(object):
    # 类属性
    china = '中国'

    # 实例属性
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

if __name__ == '__main__':
    obj = Person('vin', 20, 'male')
    print(id(obj.china), obj.china)
    print(id(Person.china), Person.china)   # 与上一行等价
    print(obj.name)

