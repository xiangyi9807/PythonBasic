#! /usr/bin/env python
# author: vin

'''
基类/父类
子类/派生类

分类：
1. 单个类继承，从下到上（优先使用自己的属性和方法）
2. 多个类继承，子类继承多个父类，从左到右
'''

class Person(object):

    gender = 'male'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('姓名：{0} 年龄：{1}'.format(self.name, self.age))

class ChinaPerson(Person):
    pass

CP = ChinaPerson('xy', 30)
CP.show()
print(CP.gender)


class ItalyPerson(Person):
    def __init__(self, name, age):
        # super(ItalyPerson, self).__init__(name, age)  与下面一行等价，建议用下面的
        Person.__init__(self, name, age)
IP = ItalyPerson('rose', 45)
print(IP.gender)
print(IP.name)
IP.show()


class SpanPerson(Person):
    def __init__(self, name, age, nation):
        self.name = name
        self.age = age
        self.nation = nation

    def show(self):
        print('姓名：{0} 年龄：{1} 国籍：{2}'.format(self.name, self.age, self.nation))

SP = SpanPerson('raul', 40, 'Spain')
SP.show()