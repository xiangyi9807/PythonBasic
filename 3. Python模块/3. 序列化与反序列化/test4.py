#! /usr/bin/env python
# author: vin

import json

# 请求数据包含字典时，先把字典序列化，再把整个请求数据序列化

request_data = {
    'name':'vin',
    'age':22,
    'datas':[
        {'city':'nanjing', 'job':'enginner'}
    ]
}

# 先序列化datas
request_data['datas'] = json.dumps(request_data['datas'])
json.dumps(request_data)