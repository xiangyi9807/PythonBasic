# -*- coding:utf-8 -*-
# xy
# 通过yield实现在单线程的情况下并发运算的效果

import time


def consumer(name):
    while True:
        print('%s 准备吃包子！' % name)
        baozi = yield
        print('包子[%s]来了，包子被[%s]吃了' % (baozi, name))


# c = consumer('vin')
# c.__next__()
# b1 = '三鲜'
# c.send(b1)      # send()方法给yield传值
# # c.__next__()


def producer():
    c1 = consumer('Vin')
    c2 = consumer('Emily')
    c1.__next__()
    c2.__next__()
    print('准备开始做包子！')
    for i in range(10):
        time.sleep(1)
        print('做了1个包子')
        c1.send(i)
        c2.send(i)


producer()