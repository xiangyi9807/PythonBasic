# -*- coding:utf-8 -*-
# xy

class Dog():
    '''
    练习
    '''
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def yap(self):
        print('汪汪汪～～')

    def run(self):
        print('%s is running' % self.name)

d1 = Dog('旺财', 3, 'male', 30)
d1.yap()
d1.run()
