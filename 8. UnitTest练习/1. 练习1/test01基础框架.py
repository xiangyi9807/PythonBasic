#! /usr/bin/env python
# author: vin

from selenium import webdriver
import unittest

class UI(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://www.baidu.com')
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        self.driver.quit()

    def test01_CheckTitle(self):
        self.assertEqual(self.driver.title, '百度一下，你就知道')

    def test02_CheckURL(self):
        self.assertIn('sina', self.driver.current_url)

if __name__ == '__main__':
    unittest.main(verbosity=2)  # verbosity控制输出的详细程度