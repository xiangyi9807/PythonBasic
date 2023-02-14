# -*- coding:utf-8 -*-
# xy

import requests

r = requests.get(url='http://www.baidu.com')
print(r.text)