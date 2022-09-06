#! /usr/bin/env python
# author: vin

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
# driver.get('')
# driver.find_element_by_id('')

def findID(driver, ID):
    return driver.find_element_by_id(ID)

def findName(driver, name):
    return driver.find_element_by_name(name)

def findTagNames(driver, tagname, index):
    return driver.find_elements_by_tag_name(tagname)[index]


driver.get('https://www.baidu.com')
findID(driver, 'kw').send_keys('python')
time.sleep(3)
driver.quit()
