'''
位置参数
关键字参数
*args
**kwargs
默认参数        -- 没有默认赋值的参数必须在前面
'''


def add(a, b=1):
    print(a+b)

add(2,3)
add(a=3, b=2)
add(2)


'''动态参数'''
print('=====================')

def foo(*args, **kwargs):
    print(args)
    print(kwargs)

foo()
foo(1)
foo(name='vin')
foo({'name':'vin'})
foo(kwargs={'name':'vin'})
foo(**{'name':'vin'})

