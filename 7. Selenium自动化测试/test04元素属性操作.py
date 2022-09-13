#! /usr/bin/env python
# author: vin

'''
get_attribute() 获取元素属性
is_displayed()  检查元素是否可见
is_enabled()    是否可编辑
is_selected()   是否被选中
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://mail.sina.com.cn/?from=mail')
driver.maximize_window()
text1 = driver.find_element(by=By.CLASS_NAME, value='placeholder').get_attribute('for')
print(text1)
text2 = driver.find_element(by=By.CLASS_NAME, value='placeholder').text
print(text2)
time.sleep(2)
driver.quit()

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
su = driver.find_element(by=By.ID, value='kw')
print(su.is_displayed())
print(su.is_enabled())
print(su.is_selected())
time.sleep(2)
driver.quit()