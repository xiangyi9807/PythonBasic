#! /usr/bin/env python
# author: vin

import time

print(time.time())
print(time.ctime(), type(time.ctime()))
print(time.ctime(time.time()))
print(time.strftime('%Y%m%d %H:%M:%S', time.localtime()))