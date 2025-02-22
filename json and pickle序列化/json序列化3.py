# -*- coding:utf-8 -*-
# xy

import json

def sayhi(name):
    print('hello', name)



info = {
    'name':'totti',
    'age':40,
    'func':sayhi
}


f = open('test3.txt', 'w')
f.write(json.dumps(info))   # 报错

f.close()