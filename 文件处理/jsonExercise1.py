# -*- coding:utf-8 -*-
# xy

# 写回文件的内容有中文时需要加上： ensure_ascii=False


import json
from pprint import pprint

with open('jsonExample', 'r') as file:
    content = json.load(file)

pprint(content)

content['shoppingList'][0]['quantity'] = 6

with open('new_jsonExample', 'w', encoding='utf-8') as file:
    json.dump(content, file, ensure_ascii=False)