#! /usr/bin/env python
# author: vin

'''
测试新浪邮箱“自动登录”是否默认勾选
'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt, unpack, data
import time

class SinaMailAutoLoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_01sina_autoLogin(self):
        isLogin = self.driver.find_element(by=By.ID, value='store1')
        self.assertTrue(isLogin.is_selected())

    def test_02sina_autoLogin(self):
        isLogin = self.driver.find_element(by=By.ID, value='store1').click()
        self.assertTrue(isLogin.is_selected())

if __name__ == '__main__':
    unittest.main()