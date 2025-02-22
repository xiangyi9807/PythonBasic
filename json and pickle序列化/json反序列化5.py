# -*- coding:utf-8 -*-
# xy

import json

f = open('test5.txt', 'r')
data = json.load(f)   # 报错
print(data)

f.close()




#  dump一次，load一次！！！
