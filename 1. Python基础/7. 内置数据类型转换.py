# 列表与字符串转换
str1 = 'hello wrold'
list1 = str1.split(' ')
print(list1)

list_str = ['a','b']
str2 = ''.join(list_str)
print(str2)

# 列表与元组之间转换
list2 = [1, 2]
tuple2 = tuple(list2)
print(tuple2, type(tuple2))

tuple3 = ('a', 'b')
list3 = list(tuple3)
print(list3, type(list3))


# 字典与列表转换
dict4 = {'name': 'vin', 'age': 12}
list4 = list(dict4)
list5 = list(dict4.items())
print(list4, type(list4))
print(list5, type(list5))

list5 = [('beijing', 10010),('tianjin', '10020')]
dict5 = dict(list5)
print(dict5, type(dict5))


# enumerate方法，返回枚举对象
list6 = ['hello', 'world']
enu = enumerate(list6, 1)
print(enu, type(enu))
dict6 = dict(enu)
print(dict6, type(dict6))

# map方法
list7 = [1,-2,3,-4,5,6]
list8 = map(abs, list7)
print(type(list8))
for i in list8:
    print(i)