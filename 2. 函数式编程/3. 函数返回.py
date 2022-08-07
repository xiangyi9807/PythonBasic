def login(username, pasword):
    if username=='vin' and pasword=='123':
        return 'tokenstr'
    else:
        return 'auth failed'

def show_order(token):
        if token == 'tokenstr':
            print('success')
        else:
            print('failed')

show_order(login('vin', '123'))
show_order(login('admin', '456'))


print('================================')

def out():
    name = input('enter name:')
    nick_name = input('enter nick name:')
    return name, nick_name

name, nick_name = out()
print(name, nick_name)
