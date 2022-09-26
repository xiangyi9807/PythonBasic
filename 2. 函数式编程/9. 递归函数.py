#! /usr/bin/env python
# author: vin


def power(n, i):
    '''
    为任意数字做幂运算
    参数：
        n 要做幂运算的数字
        i 做幂运算的次数

    :param n:
    :param i:
    :return:
    '''
    # 基线条件
    if i == 1:
        return n
    else:
        return n * power(n, i-1)

print(power(10, 2))
print(power(8, 6))
print(8 ** 6)


def fn(s):
    '''
    检查指定的字符串是否是回文
    是 返回True
    否 返回False
    参数： s 要检查的字符串
    :return:
    '''
    # 基线条件
    if len(s) < 2:
        # 字符串长度小于2，则字符串肯定是回文
        return True
    elif s[0] != s[-1]:
        # 第一个和最后一个字符不相等，肯定不是回文
        return False
    # 递归条件
    return fn(s[1:-1])

print(fn('hello'))
print(fn('abcba'))
