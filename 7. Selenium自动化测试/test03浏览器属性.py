#! /usr/bin/env python
# author: vin

'''
切换窗口
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://mail.sina.com.cn/?from=mail')
driver.maximize_window()
nowhandler = driver.current_window_handle
driver.find_element(by=By.LINK_TEXT, value='注册').click()
handlers = driver.window_handles
print(nowhandler)
time.sleep(3)
for handle in handlers:
    # print(handle)
    if handle != nowhandler:
        driver.switch_to.window(nowhandler)
        time.sleep(3)
driver.quit()