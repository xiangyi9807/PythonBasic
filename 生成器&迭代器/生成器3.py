# -*- coding:utf-8 -*-
# xy

# 斐波那契函数变为生成器


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a+b
        n += 1
    return 'done'       # 不加这句的情况下，一直用__next__()超出范围会抛出异常

a = fib(100)
print(a)

print('==================================')

print(a.__next__())
print(a.__next__())
print(a.__next__())
# 可以同步处理其他任务，实现多线程
print(a.__next__())
print(a.__next__())
print(a.__next__())
print('=============start loop============')
for i in a:
    print(i)


print('==================================')
# 如果不加return 'done',用循环获取时加入try except


b = fib(20)
while True:
    try:
        x = next(b)
        print('g:', x)
    except StopIteration as e:
        print('generator return value:', e.value)
        break