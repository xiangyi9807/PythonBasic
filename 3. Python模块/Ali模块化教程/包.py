#! /usr/bin/env python
# author: vin

'''
包也是一个模块
模块中的代码过多或模块需要被分解成多个时使用
普通的模块是一个.py文件，包是一个文件夹
包中必须有个__init__.py文件，这个文件包含包中的重要内容
'''

'''
import package_test01

# print(package_test01.a)
package_test01.test()
'''

from package_test01 import a,b
print(a.c)
print(b.d)


'''
__pycache__是模块的缓存文件
py代码在执行前，需要被解析成机器码，然后再执行
使用模块/包时也需要先转成机器码，再执行
为了提高程序运行性能，python会在编译过一次之后将代码保存到一个缓存文件中
下次加载模块/包时不再重新编译，直接加载缓存中编译好的代码
'''