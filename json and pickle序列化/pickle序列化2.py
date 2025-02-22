# -*- coding:utf-8 -*-
# xy

import pickle

def sayhi(name):
    print('hello', name)


info = {
    'name':'totti',
    'age':40,
    'func':sayhi
}

f = open('test4.txt', 'wb')
pickle.dump(info, f)
f.close()


