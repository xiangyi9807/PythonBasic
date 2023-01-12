#! /usr/bin/env python
# author: vin

# 输出到控制台

import logging

def logTest():
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.DEBUG)
    # 定义格式
    log_format = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    # 控制台的输出
    fh_stream = logging.StreamHandler()
    fh_stream.setLevel(logging.DEBUG)
    fh_stream.setFormatter(fmt=log_format)
    # 写进文件
    fh_file = logging.FileHandler('log2.log', 'a', encoding='utf-8')
    fh_file.setFormatter(logging.DEBUG)
    fh_file.setFormatter(fmt=log_format)
    # 添加到handler里
    logger.addHandler(fh_stream)
    logger.addHandler(fh_file)
    return logger

logTest().debug('debug log test')
# logTest().info()