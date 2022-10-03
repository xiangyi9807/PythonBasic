#! /usr/bin/env python
# author: vin

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

    # @unittest.skip('忽略执行测试')
    def test02_CheckURL(self):
        self.assertIn('sina', self.driver.current_url)

class Demo(unittest.TestCase):
    def test_001(self):
        pass
    def test_002(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)  # verbosity控制输出的详细程度，有多个测试类的时候会全部执行
    # suite = unittest.TestSuite()
    # suite.addTest(UI('test01_CheckTitle'))
    # # suite.addTest(UI('test02_CheckURL'))
    # unittest.TextTestRunner(verbosity=2).run(suite)