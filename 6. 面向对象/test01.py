#! /usr/bin/env python
# author: vin

'''
java: 单继承
pthon: 可以继承多个类
类名首字母大写，驼峰方式

执行顺序：
1. 实例化
2. 调用类方法
3. 析构

类属性:属于类，但是也可以使用对象调用，结果是等价的，建议类调用
实例属性，属于对象，只能使用对象调用


封装
1. 把同等操作的行为封装到一个类之中，方便管理
2. 把公共的属性（变量）封装到类的初始化操作中（封装到类的构造方法）

方法
1. 普通方法，属于对象
2. 特性方法，带装饰器，属于对象，不带括号，不能用参数
3. 静态方法，不带self，属于类也属于对象，强烈建议类直接调用
4. 类方法
'''

# 新式类
class UsePersonTest(object):
    # 构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('初始化方法')

    # 析构方法
    def __del__(self):
        print('执行结束')

    def info(self):
        print('hello world!')

if __name__ == '__main__':
    obj = UsePersonTest('vin', 20)
    obj.info()