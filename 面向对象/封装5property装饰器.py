#! /usr/bin/env python
# author: vin

# setter和getter方法必须成对出现

class Person():
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # property装饰器，用来将一个get方法，转换为对象的属性
    # 添加完property装饰器，可以像调用属性一样使用get方法
    # 使用property方法装的方法，必须和属性名一样
    @property
    def name(self):
        # print('调用了方法')
        return self._name


    # setter方法的装饰器：@属性名.setter
    @name.setter
    def name(self, new_name):
        # print('调用了setter方法')
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

p = Person('tom', 10)
print(p.name, p.age)
p.name = 'jerry'
p.age = 12
print(p.name, p.age)