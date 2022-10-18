#! /usr/bin/env python
# author: vin


import unittest
import os
import HTMLTestRunner
import time

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

def getNow():
    return time.strftime('%Y%m%d%H%M%S', time.localtime())

# print(getNow())

def runtest():
    filename = getNow()+'-report.html'
    runner = HTMLTestRunner.HTMLTestRunner(
        stream = open(filename, 'wb'),
        verbosity = 2,
        title = '自动化测试报告',
        description= '报告详细描述'
    ).run(getSuites())


if __name__ == '__main__':
    runtest()