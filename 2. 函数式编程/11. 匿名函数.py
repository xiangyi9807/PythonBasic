#! /usr/bin/env python
# author: vin


'''
filter
参数： 函数，可迭代对象
作用：按函数执行结果把可迭代对象里所有结果是true的元素返回到一个新的可迭代对象
'''
l = [1,2,3,4,5,6,7,8,9,10]

def fn(n):
    if n%2 == 0:
        return True
    return False

new_lst = filter(fn, l)
print(list(new_lst))


'''
lambda:用来创建简单函数
语法： lambda 参数列表:返回值
'''


print((lambda a,b : a+b)(1,2))


r = filter(lambda i: i>5, l)
print(list(r))


'''
map
参数：函数，可迭代对象
作用：对可迭代对象里的所有元素按函数定义的做指定操作，添加到一个新的可迭代对象里
'''

def fn1(i):
    return i**2

m = map(fn1, l)
print(list(m))

n = map(lambda i:i**2, l)
print(list(n))