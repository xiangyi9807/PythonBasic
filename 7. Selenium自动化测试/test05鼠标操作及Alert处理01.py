#! /usr/bin/env python
# author: vin

# 百度首页，鼠标悬浮，点击保存网络设置，获取alert内容

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
settings = driver.find_element(by=By.XPATH, value='//*[@id="s-usersetting-top"]')
alert = Alert(driver)
Action = ActionChains(driver)
# 鼠标悬浮到【设置】上
Action.move_to_element(settings).perform()
time.sleep(3)
# 点击【搜索设置】
driver.find_element(by=By.XPATH, value='//*[@id="s-user-setting-menu"]/div/a[1]/span').click()
time.sleep(3)
# 点击保存
driver.find_element(by=By.XPATH, value='//*[@id="se-setting-7"]/a[2]').click()
time.sleep(2)
# 获取alert文本
alert_text = driver.switch_to.alert.text
print(alert_text)
driver.switch_to.alert.accept()
driver.quit()