list1 = list(range(10))
# print(list1)

list2 = list(map(abs, list1))
print(list2)


print('================================')

def foo(x):
    return x+10

list3 = list(map(foo, list1))
print(list3)


print('================================')

list4 = list(map(lambda x:str(x), list1))
print(list4)