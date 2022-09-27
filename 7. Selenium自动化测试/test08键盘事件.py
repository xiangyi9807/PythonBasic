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
# ctrl + A
target.send_keys(Keys.CONTROL, 'a')
time.sleep(2)
# ctrl + C
target.send_keys(Keys.CONTROL, 'c')
time.sleep(2)
# backspace
target.send_keys(Keys.BACKSPACE)
time.sleep(2)
# ctrl + V
target.send_keys(Keys.CONTROL, 'v')
time.sleep(2)
# enter
target.send_keys(Keys.ENTER)
time.sleep(2)
driver.refresh()
driver.quit()