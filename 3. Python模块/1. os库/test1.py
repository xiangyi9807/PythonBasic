#! /usr/bin/env python
# author: vin

import os
# print(os.__all__)

# print(os.getcwd())  # 模块的当前路径
# print(os.system('ping https://www.baidu.com'))  # 执行系统命令
# print(os.getpid())  # 获取进程

# 获取文件夹下所有文件（包括隐藏文件）
# for item in os.listdir('c:/'):
#     print(item)

# print(os.path.exists('c:/python'))  # 判断路径存在不存在
# print(os.path.isfile('c:/'))    # 判断是不是文件
# print(os.path.isdir('c:/'))     # 判断是不是路径

# print(os.path.dirname(os.path.dirname(os.path.abspath('__file__'))))

# 使用拼接的方式获取下级目录
file_path = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
print(os.path.join(file_path, '1. os库'))
