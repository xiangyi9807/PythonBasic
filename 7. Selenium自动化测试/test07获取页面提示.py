#! /usr/bin/env python
# author: vin

'''

'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://mail.sina.com.cn/')
driver.maximize_window()
driver.find_element(by=By.CLASS_NAME, value='loginBtn').click()
#错误路径，验证是否真的检查了，会报错
# WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH, '/html/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]'),'请输入邮箱名'))
#对比的文案错误时,会报错
# WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]'),'测试错误对比文案'))
#正确路径
WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]'),'请输入邮箱名'))
driver.quit()