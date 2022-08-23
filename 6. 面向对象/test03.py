#! /usr/bin/env python
# author: vin

class Person(object):

    def show(self):
        print('姓名：{0}'.format(self.name))

if __name__ == '__main__':
    obj = Person()
    obj.name = 'vin'
    obj.show()
