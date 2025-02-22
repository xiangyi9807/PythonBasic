# -*- coding:utf-8 -*-
# xy

# 实现不同变成语言间序列化与反序列化

import pickle

def sayhi(name):
    print('hello', name)


info = {
    'name':'totti',
    'age':40,
    'func':sayhi
}


f = open('test3.txt', 'wb')
f.write(pickle.dumps(info))

f.close()


# 同一个文件里能反序列化

f = open('test3.txt', 'rb')
data = pickle.loads(f.read())  # 报错，sayhi程序在前一个文件运行完后就被释放了
print(data)
data['func']('totti')