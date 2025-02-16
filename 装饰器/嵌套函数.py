# -*- coding:utf-8 -*-
# xy

# 函数嵌套：在一个函数中用def去声明另外一个函数


def foo():
    print('in the foo')

    def bar():
        print('in the bar')

    bar()


foo()


x = 0


def grandpa():
    x = 1

    def dad():
        x=2

        def son():
            x = 3
            print(x)
        son()
    dad()


grandpa()