#! /usr/bin/env python
# author: vin

'''
open api: 开放平台
如 微博和百度的open api
有些open api会要求对请求的参数做ascii排序并处理成urlcode，再做md5加密，加密后的内容给sign，最后做请求
1. ascii排序: sorted() + **kwargs
2. urlcode parse name=vin
3. md5加密: hashlib
4. sign
'''

import hashlib
from urllib import parse

def getSign(**kwargs):
    dict1 = sorted(kwargs.items(), key=lambda itme:itme[0])  #对key做排序
    # print(dict1)
    datas = parse.urlencode(dict1)
    # print(datas)
    md5 = hashlib.md5()
    md5.update(datas.encode('utf-8'))
    return md5.hexdigest()      # md5加密


print(getSign(**{'name':'vin', 'age':20}))
