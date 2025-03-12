# -*- coding:utf-8 -*-
# xy


def hui_wen(s):
    '''
    该函数判断指定的字符串是否是回文(abcdcba)，返回Ture 或 False
    先检查第一个和最后一个字符是否一致，如果不一致返回False
    继续检查剩余的字符是否一致

    :return:
    '''
    if len(s) < 2:
        return True
    elif s[0] != s[-1]:
        return False

    return hui_wen(s[1:-1])

print(hui_wen('abcde'))
print(hui_wen('abcba'))

