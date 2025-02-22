# -*- coding:utf-8 -*-
# xy

# hex() 转16进制
print(hex(15))
print(hex(255))


# locals()
def foo():
    local_var = 1
    print(locals())
    print(globals())
print(globals())
foo()


# oct() 转八进制
print(oct(16))


# repr() 用字符串表示对象
print(repr(foo))


# round() 保留几位小数
print(round(1.234, 2))


# sorted()
a = {6:2, 8:0, 1:4, -5:6, 99:11, 4:22}
print(a)
print(sorted(a.items()))    # 默认按key排序
print(sorted(a.items(), key=lambda x:x[1]))     # 按value排序


# zip()
a = [1,2,3,4]
b = ['a','b','c']
print(zip(a,b))
for i in zip(a,b):
    print(i)