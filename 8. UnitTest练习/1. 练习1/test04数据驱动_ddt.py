#! /usr/bin/env python
# author: vin

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from ddt import ddt, unpack, data
import time

@ddt
class SinaMailLoginTest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://mail.sina.com.cn/')
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    @data(
        ('','','请输入邮箱名'),
        ('assss@sina.com', 'pssss', '登录名或密码错误')
    )
    @unpack
    def test_add_result(self, username, password, result):
        self.driver.find_element(by=By.ID, value='freename').send_keys(username)
        self.driver.find_element(by=By.ID, value='freepassword').send_keys(password)
        time.sleep(2)
        self.driver.find_element(by=By.LINK_TEXT, value='登录').click()
        time.sleep(2)
        tips = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[2]/div/div/div[4]/div[1]/div[1]/div[1]/span[1]').text
        self.assertEqual(tips, result)

if __name__ == '__main__':
    unittest.main()