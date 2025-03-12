# -*- coding:utf-8 -*-
# xy

'''
闭包的条件：
1.函数嵌套
2.内部函数作为返回值返回
3.内部函数必须要使用外部函数的变量
'''

def make_averager():
    nums = []
    def averager(n):
        nums.append(n)
        return sum(nums)/len(nums)
    return averager

averager = make_averager()
print(averager(10))
print(averager(20))
print(averager(30))
print(averager(40))
print(averager(50))