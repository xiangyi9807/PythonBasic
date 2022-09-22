#! /usr/bin/env python
# author: vin
'''
1. 显示等待
2. 隐士等待
3. 强制等待
'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://mail.sina.com.cn/')
driver.implicitly_wait(30)
# WebDriverWait(driver=driver, timeout=2).until(EC.element_to_be_selected((By.ID, 'kw')))
# WebDriverWait(driver=driver, timeout=20).until(EC.visibility_of_element_located((By.ID, 'kw')))
# WebDriverWait(driver=driver, timeout=3).until(EC.url_contains('google'))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, '新浪首页'))).click()
driver.quit()