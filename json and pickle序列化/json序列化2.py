# -*- coding:utf-8 -*-
# xy

import json

info = {
    'name':'totti',
    'age':40
}

f = open('test2.txt', 'w')
f.write(json.dumps(info))
f.close()


f = open('test2.txt', 'r')
data = json.loads(f.read())
print(data['name'])