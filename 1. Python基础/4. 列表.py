list1 = [1,2,3,4,5]

# 找出大于3的元素组成新的列表，方法1
list2 = []
for i in list1:
    if i>2:
        list2.append(i)
    else:
        pass
print(list2)

# 找出大于3的元素组成新的列表，方法2，列表推导式
list3 = [i for i in list1 if i>2]
print(list3)