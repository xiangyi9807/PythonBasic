#! /usr/bin/env python
# author: vin

import json
import requests

r= requests.get(url='http://t.weather.sojson.com/api/weather/city/101030100')

print(json.dumps(r.json(), ensure_ascii=False, indent=True))    # r.json()返回字典， ensure_ascii=False 显示中文， indent=True 缩进格式
