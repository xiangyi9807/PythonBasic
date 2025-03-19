#! /usr/bin/env python
# author: vin

class A():
    def test(self):
        print('实例方法，', self)

    @classmethod
    def test2(cls):
        print('类方法，', cls)

    # 静态方法不需要任何默认参数，可以通过类和实例去调用
    # 静态方法基本上是和当前类无关的方法
    @staticmethod
    def test3():
        print('静态方法')


a = A()
A.test(A)
a.test()
A.test2()
a.test2()
A.test3()
a.test3()