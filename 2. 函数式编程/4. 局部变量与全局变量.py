username = 'vin'

def info():
    username = 'admin'
    print(username)

info()
print(username)


print('=====================================')
'''修改全局变量的值'''

name = 'adam'

def new_name():
    global name
    name = 'jerry'
    print(name)

new_name()
print(name)