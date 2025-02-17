# -*- coding:utf-8 -*-
# xy

user,passwd = 'vin','abc123'


def auth(authtype):
    print('authtype:', authtype)

    def outer_wrapper(func):
        print('auth func:', func)

        def wrapper(*args, **kwargs):
            print('wrapper func args:', args, kwargs)
            if authtype == 'local':
                usernmae = input('enter username:').strip()
                password = input('enter password:').strip()
                if user==usernmae and passwd==password:
                    print('\033[32:1mUser has passed authentication\033[0m')
                    res = func(*args, **kwargs)
                    print('after authentication')
                    return res
                else:
                    exit('\033[31:1mInvalid username or password\033[0m')
            elif authtype == 'ldap':
                print('ldap auth...')
        return wrapper
    return outer_wrapper


def index():
    print('welcome to index page')


@auth(authtype='local')
def home():
    print('welcome to home page')
    return 'from home'


@auth(authtype='ldap')
def bbs():
    print('welcome to bbs page')


index()
# home()
print(home())
bbs()