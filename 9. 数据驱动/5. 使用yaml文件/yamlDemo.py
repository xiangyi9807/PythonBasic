#! /usr/bin/env python
# author: vin

'''
安装PyYaml库

'''

import yaml

def readYaml():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        r = yaml.safe_load(f)
        # print(r)
        # print(type(r))
        return r

data = readYaml()
print(data)
print(type(data))
print(data['datas'])