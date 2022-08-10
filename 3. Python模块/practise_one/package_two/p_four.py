#! /usr/bin/env python
# author: vin

import sys
import os

file_path = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
# print(file_path)
# os.path.dirpath
sys.path.append(file_path)

from package_one import p_two
print(p_two.str1)