#! /usr/bin/env python
# author: vin

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print('Class Person')


class ChinaPerson(Person):
    def __init__(self, name, age, nation):
        Person.__init__(self, name, age)
        self.nation = nation

    def show(self):
        print('ChinaPerson')


class XJPerson(ChinaPerson):
    def __init__(self, name, age, nation, language):
        ChinaPerson.__init__(self, name, age, nation)
        self.language = language

    def show(self):
        print('姓名：{0} 年龄：{1} 国家：{2} 语言：{3}'.format(self.name, self.age, self.nation, self.language))


if __name__ == '__main__':
    XJP = XJPerson('vin', 39, 'CHN', 'seno')    # 如果子类没有重写父类方法，则从左到右继承父类的方法
    XJP.show()