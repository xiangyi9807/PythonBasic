#! /usr/bin/env python
# author: vin

# 多态：如果一个东西，走路像鸭子，叫声像鸭子，那么它就是鸭子
class A:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class B:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


class C:
    pass

a = A('tom')
b = B('jerry')
c= C()


# 只要有name属性的对象都可以作为参数传递
def say_hello(obj):
    print('hello %s' % obj.name)


say_hello(a)
# say_hello(c)


# 加入类型检查，违反了多态，无法处理其他类型对象，适用性差
def say_hello_2(obj):
    if isinstance(obj, A):
        print('hello %s' % obj.name)


say_hello_2(a)
say_hello_2(b)