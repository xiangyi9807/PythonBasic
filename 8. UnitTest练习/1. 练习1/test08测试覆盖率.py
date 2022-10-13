#! /usr/bin/env python
# author: vin

'''
使用第三方包coverage

进入py文件所在路径，cmd窗口命令：
coverage run test1.py
coverage report
coverage html    --> 在当前文件夹下创建htmldoc文件夹并生成html文件

打开html文件，点击.py文件可以查看那些代码行没有被测试覆盖到
目标是100%覆盖
'''

import unittest
from ddt import ddt, data, unpack

def sum(a,b):
    try:
        return a+b
    except Exception as e:
        print(e.args[0])

@ddt
class test_01(unittest.TestCase):
    @data(
        (1, 2, 3),
        (1.1, 2.0, 5.0),
        (1, 'a', '1a'),
        ('hello', 'world', 'hello world')
    )
    @unpack
    def test_01(self, a, b, result):
        self.assertEqual(sum(a,b), result )


if __name__ == '__main__':
    unittest.main()