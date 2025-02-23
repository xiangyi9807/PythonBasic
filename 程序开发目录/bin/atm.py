# -*- coding:utf-8 -*-
# xy

import os
import sys

# 打印当前文件相对路径，在pycharm里可以打印绝对路径
print(__file__)
# 打印绝对路径
print(os.path.abspath(__file__))
# 获取上级目录
print(os.path.dirname(os.path.abspath(__file__)))
# 再获取上级目录
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# 添加到环境变量
sys.path.append(BASE_DIR)


# import conf, core
from conf import settings
from core import main

main.login()