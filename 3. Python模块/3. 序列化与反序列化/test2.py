#! /usr/bin/env python
# author: vin

import json

# 对列表做序列化处理
list1 = [1,2,3,4,5,6]
list_str = json.dumps(list1)
print(list_str, type(list_str))

# 反序列化处理
str_list = json.loads(list_str)
print(str_list, type(str_list))

print('=======================================')

# 元组的序列化与反序列化
tuple1 = (1,2,3)
tuple_str = json.dumps(tuple1)
print(tuple_str, type(tuple_str))
str_tuple1 = json.loads(tuple_str)
print(str_tuple1, type(str_list))

print('=======================================')

# 字典的序列化与反序列化
dict1 = {'status':200, 'msg':'ok', 'datas':[{'name':'vin'}]}
dict_str = json.dumps(dict1)
print(dict_str, type(dict_str))
str_dict = json.loads(dict_str)
print(str_dict, type(str_dict))