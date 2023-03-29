# json： 字符串格式的字典

dict1 = {'name':'vin', 'age':20}
# print(dir(dict1))

# 增加
dict1['job'] = 'engineer'
print(dict1)

# 删除
dict1.pop('name')
print(dict1)

# 修改
dict1['age'] = 25
print(dict1)

# 遍历
for key, values in dict1.items():
    print(key, values)

dict2 = {'itme1':{'age':20}, 'item2':[1,2,3]}
for key, values in dict2.items():
    print(key, values)

# 合并
dict2.update(dict1)
print(dict2)

# 排序后返回列表
print(sorted(dict2.items(), key= lambda item:item[0]))


'''判断key是否在字典'''

dict5 = {'name':'vin', 'age':12}

if 'name' in dict5:
    print('y')