#! /usr/bin/env python
# author: vin

'''
内置方法：
__init__: 用于类对象初始化
__del__: 析构方法，类中的方法执行后会执行该方法
__doc__: 类的描述信息
__str__: 改变对象的字符创显示
__call__: 类对象后面加（），就触发该内置方法
'''

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
        '''返回字符串的对象'''
        return '调用str方法__姓名:{0}，年龄：{1}'.format(self.name, self.age)

if __name__ == '__main__':
    obj = Person('vin', 20)
    print(obj)
    # print(obj())
    # print(obj.__doc__)
    # print(obj.__call__)
