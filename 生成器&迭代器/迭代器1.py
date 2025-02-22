# -*- coding:utf-8 -*-
# xy
# 可以直接作用于for循环的对象统称可迭代对象Iterable包括：
# 1.集合数据类型（list,tuple,dict,set,str）
# 2.generator,包括生成器和带yield的generator function
# 可以使用isinstance()判断一个对象是否是Iterable对象


from collections.abc import Iterable
print(isinstance([], Iterable))
print(isinstance('abc', Iterable))
print(isinstance((i*2 for i in range(10)), Iterable))


print('========================================')


# 可以被next()函数调用并不断返回下一个值的对象统称为迭代器 Iterator
from collections.abc import Iterator
print(isinstance([1,2,3], Iterator))
print(isinstance((i for i in range(10)), Iterator))


print('========================================')


# 生成器都是Itretor对象，但list,tuple,set,dict,str虽然是Iterable，但不是Iterator
# 把list,set,dict变成Iterator，可以使用iter()函数
print(isinstance(iter([1,2,3]), Iterator))