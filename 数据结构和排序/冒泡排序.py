# -*- coding:utf-8 -*-
# xy

import random

lst = []
for i in range(20):
    lst.append(random.randint(1,100))

print(lst)

n = 0
while True:
    for i in range(len(lst)-1):
        if lst[i] < lst[i+1]:
            pass
        else:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    n += 1
    if n == len(lst)-1:
        break


print(lst)