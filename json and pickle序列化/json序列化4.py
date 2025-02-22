# -*- coding:utf-8 -*-
# xy

import json

info = {
    'name':'totti',
    'age':40,
}


f = open('test5.txt', 'w')
json.dump(info, f)


info['age'] = 35

json.dump(info, f)
f.close()