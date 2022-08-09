list1 = [1,2,3,4,5]

def foo(x):
    if x>2:
        return x

list2 = filter(foo, list1)

print(list2)

for i in list2:
    print(i)

print('================================')

list3 = [1,2,3,4,5,6,7,8,9]
list4 = list(filter(lambda x:x%2==0, list3))
print(list4)