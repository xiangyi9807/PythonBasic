# -*- coding:utf-8 -*-
# xy

# 列表生成式
a = [1, 2, 3]
print(a)

list1 = [i*2 for i in range(10)]
print(list1)

print('==================================')


def func(n):
    return n

list2 = []
list2.append([func(i) for i in range(10)])
print(list2)

print('==================================')


# 列表生成器（一边循环一边计算的机制，叫生成器）
# 生成器只有在调用时才会生成相应的数据
# __next__()方法，或者循环遍历
print(range(5))

list3 = (x for x in range(20))
for i in list3:
    print(i, end=' ')

print()

print('==================================')

