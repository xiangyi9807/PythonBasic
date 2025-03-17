#! /usr/bin/env python
# author: vin

# 方法重写
# 父类的所有方法都会被子类继承，包括特殊方法，也可以重写特殊方法

class Animal():
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def run(self):
        print('Animal running~~')

    def sleep(self):
        print('Animal sleeping~~')


class Dog(Animal):
    def __init__(self, name, age):
        # self._name = name
        # Animal.__init__(self, name)   # 不要写死Animal，如果换了父类会报错
        # 使用super()获取当前类的父类，通过super()方法可以不用传self
        super().__init__(name)
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        self._age = new_age

    def run(self):
        print('Dog %s running~~' % self.name)

    def bark(self):
        print('Dog barking~~')


d1 = Dog('旺财', 3)
d1.run()
d1.age = 5
print(d1.age)