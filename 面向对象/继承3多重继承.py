#! /usr/bin/env python
# author: vin

class A(object):
    def test(self):
        print('AAA')


class B(object):
    def test(self):
        print('test func in B')

    def test2(self):
        print('BBB')


# 多重继承，一个类可以有多个父类
# 多个父类有同名方法，会先在第一个父类寻找，然后依次类推
class C(A, B):
    pass

# __bases__ 隐藏属性，可以获取当前类的所有父类
print(C.__bases__)
c1 = C()
c1.test()
c1.test2()