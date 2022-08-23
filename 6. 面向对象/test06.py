#! /usr/bin/env python
# author: vin

class Person(object):
    def __init__(self, name):
        self.name = name

    def api(self, **kwargs):
        print(kwargs)

    def show(self):
        print(self.name)

    def info(self, nation='China'):
        print('姓名：{0}, 国籍：{1}'.format(self.name, nation))

if __name__ == '__main__':
    obj = Person('vin')
    obj.show()
    obj.api(**{'name':'jerry'})
    obj.api(**{'name': 'jerry', 'age':20})
    obj.info()
    obj.info('Italy')
