# -*- coding:utf-8 -*-
# xy

# 函数即变量


def bar():
    print('in the bar')


def foo():
    print('in the foo')
    bar()


foo()


print('###########################################')


def foo1():
    print('in the foo')
    bar()


def bar1():
    print('in the bar')


foo1()


print('###########################################')


def foo2():
    print('in the foo')
    bar()


foo2()


def bar2():
    print('in the bar')


