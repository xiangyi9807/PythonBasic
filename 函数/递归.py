# -*- coding:utf-8 -*-
# xy

def power(n, i):
    if i == 1:
        return n
    else:
        return n * power(n, i-1)


print(pow(5, 3))