#! /usr/bin/env python
# author: vin

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
driver.maximize_window()
driver.implicitly_wait(30)
target = driver.find_element(by=By.ID, value='kw')
target.send_keys('webdriver')
time.sleep(1)
target.send_keys(Keys.ENTER)
time.sleep(3)

# 滚动页面到底部的js语句
scroll_down = 'document.documentElement.scrollTop = 10000'
# 滚动页面到顶部的js语句
scroll_top = 'document.documentElement.scrollTop = 0'
driver.execute_script(scroll_down)
time.sleep(2)

# 翻页操作
driver.find_element(by=By.LINK_TEXT, value='下一页 >').click()
time.sleep(2)

driver.quit()