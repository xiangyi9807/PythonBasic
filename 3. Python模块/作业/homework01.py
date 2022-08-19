#! /usr/bin/env python
# author: vin

'''
取出列表中大于3的元素
[1,2,3,4,5,6,7,8,9,10]
'''

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = []
for i in list1:
    if i>3:
        list2.append(i)
print(list2)

list3 = list(filter(lambda x:x>3, list1))
print(list3)