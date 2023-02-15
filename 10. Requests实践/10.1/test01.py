#! /usr/bin/env python
# author: vin

import requests

r = requests.request(method='get', url='http://www.baidu.com')
print(r.status_code)
# print(r.text)
# print(r.content)
print(r.url)
print(r.headers)