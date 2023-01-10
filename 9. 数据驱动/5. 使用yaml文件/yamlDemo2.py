#! /usr/bin/env python
# author: vin

'''
安装PyYaml库

'''

import yaml

def readYaml():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        r = yaml.safe_load_all(f)
        # print(r)
        # print(type(r))
        for item in r:
            return item

print(readYaml())