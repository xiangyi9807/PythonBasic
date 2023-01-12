#! /usr/bin/env python
# author: vin

import logging

logging.basicConfig(filename='log1.txt',
                    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                    datefmt='%Y-%m-%d',
                    level=5)

logging.info('info log test')
logging.debug('debug log test')
logging.warn('warm log test')
logging.error('error log test')