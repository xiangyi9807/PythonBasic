#! /usr/bin/env python
# author: vin

import sys
# sys.argv 获取执行代码时，命令行所包含的参数（cmd窗口里执行，后面可以手动加参数），返回列表
# print(sys.argv)
# sys.modules 获取当前程序中引入的所有模块，返回字典
# print(sys.modules)

'''
pprint模块，提供pprint()方法，用于打印数据的格式化
'''
import pprint
# pprint.pprint(sys.modules)

# sys.path 保存模块搜索路径的列表
# pprint.pprint(sys.path)

# sys.platform 标识python运行的平台
# print(sys.platform)

# sys.exit()    退出程序
# sys.exit('exit, bye...')

import os
pprint.pprint(os.path)
# os.environ 获取系统环境变量
# print(os.environ)
# print(os.environ['path'])
# os.system()   执行系统命令
os.system('dir')
os.system('notepad')