#! /usr/bin/env python
# author: vin

'''
模块引入
    1. import 模块名（.py文件）
        1.1 可以多次引入同一个模块，但模块的实例只会创建一个
    2. import xxx as xxx
    3. from xxx import xxx
'''

import module_test01
# import module_test01

print(module_test01)
print(module_test01.__name__)
print(__name__)