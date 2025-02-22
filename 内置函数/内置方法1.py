#! /usr/bin/env python
# author: vin

# all() 可迭代对象里所有元素都是真就返回True,否则返回False
print(all([1,2,3]))
print(all((i for i in range(10))))


# any() 可迭代对象里任意元素都是真就返回True,没有元素返回False
print(any([1,2,3]))
print(any((i for i in range(10))))
print(any([]))


# ascii() 返回字符串格式
print(ascii('abc'))
print(ascii([1,'a','中国']))
print(type(ascii([1,'a','中国'])))


# bin() 十进制数字转二进制
print(bin(1))
print(bin(2))
print(bin(255))


# bytearray()  字节数组，可修改！！
a = bytes('abcde', encoding='utf-8')
print(a)
print(a.capitalize())
print(a)
b = bytearray('abcde', encoding='utf-8')
print(b[0])
b[0] = 100   # ascii编码编号
print(b)


# callable() 判断是否可调用
print(callable(['']))
def foo():
    pass
print(callable(foo))


# chr()返回字符的ascii编码对应的字母
print(chr(100))
print(ord('a'))


# compile()
code = '''
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n += 1
    return 'done'


fib(100)
'''
py_obj = compile(code, 'err.log', 'exec')       # 如果失败，则把日志写入err.log文件
exec(py_obj)        # exec方法也可以直接运行code


# dir()
a = {}
print(dir(a))


# divmod() 相除返回商和余数
print(divmod(5, 3))

# eval() 字符串转字典


# filter()  过滤数据
(lambda n:print(n))(5)
calc = lambda n:print(n*2)
calc(5)
res = filter(lambda n:n>5, range(10))
for i in res:
    print(i)


# map() 对传入的每个值做处理
res = map(lambda n:n**2, range(10))
for i in res:
    print(i)


# reduce()
import functools
res = functools.reduce(lambda x,y:x+y, range(10))   # 累加
# res = functools.reduce(lambda x,y:x*y, range(1,10))   # 阶乘
print(res)


# forzenset() 冻结set，不允许再有pop clear之类的方法
a = set([1,2,3,3,4,5,6])
a.pop()
b = frozenset([1,2,3,3,4,5,6])
b.copy()


# globals() 返回当前程序中的所有全局变量，字典格式
print(globals())


# hash() 散列值算法，md5是hash的一种算法
print(hash('abc'))
print(hash('abc'))
print(hash('abc'))  # 同样的数据使用hash永远算出来的都是一个值，折半查找