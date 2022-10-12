#! /usr/bin/env python
# author: vin

import unittest
import os

def getSuites():
    '''
    获取所有测试用例
    :return:
    '''
    suites = unittest.defaultTestLoader.discover(
        start_dir = os.path.dirname(__file__),
        pattern = 'test*.py',
        top_level_dir = None
    )
    return suites

suites = getSuites()
caseList = []

for package in suites:
    for moudle in package:
        for cases in moudle:
            print(cases)
            caseList.append(cases)

print('测试用例数量{0}'.format(len(caseList)))