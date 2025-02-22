# -*- coding:utf-8 -*-
# xy

import pickle

f = open('test3.txt', 'rb')
data = pickle.loads(f.read())  # 报错，sayhi程序在前一个文件运行完后就被释放了，除非再当前文件复制一个sayhi函数
print(data)