#! /usr/bin/env python
# author: vin

import json
import requests

# 对文件序列化，把内容写进文件
# json.dump()
# 对文件反序列化，把文件内容读取出来
# json.load()

# r = requests.get(url='http://t.weather.sojson.com/api/weather/city/101030100')
# # 把返回数据写入文件
# json.dump(r.text, open('weather.json', 'w'))


# 对文件做反序列化
content = json.load(open('weather.json', 'r'))
# print(content)
content = json.loads(content)   #反序列化为字典
# print(type(content))
# print(json.dumps(content, indent=True))
print(content['cityInfo']['city'])  #判断获取的城市