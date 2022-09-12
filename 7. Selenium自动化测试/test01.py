#! /usr/bin/env python
# author: vin

'''
1. 单个元素定位
2. 多个元素定位
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

'''
ID = "id"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
NAME = "name"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"
'''

keywords = ['python', '迪丽热巴',]
for item in keywords:
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    # driver.find_element_by_id()
    driver.find_element(by=By.ID, value='kw').send_keys(item)
    driver.find_element(by=By.ID, value='su').click()
    time.sleep(3)
    driver.quit()