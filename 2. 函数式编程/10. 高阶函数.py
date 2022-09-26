#! /usr/bin/env python
# author: vin

'''
函数式编程
在python中，函数式一等对象，有以下特点：
1. 对象是在运行时创建
2. 能赋值给变量或作为数据结构中的元素
3. 能作为参数传递
4. 能作为返回值返回

高级函数（至少符合以下两个特点中的一个）
1. 接收一个或多个函数作为参数
2. 将函数作为返回值返回

pyhon支持函数式编程，但不是函数式编程语言
'''

l = [1,2,3,4,5,6,7,8,9,10]

def fn1(n):
    if n%2 == 0:
        return True
    return False

def fn2(n):
    if n>5:
        return True
    return False

def fn(func, lst):
    '''
    功能：
        将指定列表中的所有符合条件的元素取出来
        保存到新列表
    参数：
        lst，要进行筛选的列表
    :return:
    '''
    new_lst = []
    for i in lst:
        if func(i):
            new_lst.append(i)
    print(new_lst)

fn(fn1, l)
fn(fn2, l)