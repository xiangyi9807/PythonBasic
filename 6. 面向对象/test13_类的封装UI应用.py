#! /usr/bin/env python
# author: vin

from selenium import webdriver
import time

class UI(object):
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.implicitly_wait(30)

    def findID(self, ID):
        '''注意别用小写的id，因为id是python的关键字'''
        return self.driver.find_element_by_id(ID)

    def sendKeys(self, ID, keywords):
        self.findID(ID).send_keys(keywords)

    def __del__(self):
        self.driver.quit()

if __name__ == '__main__':
    obj = UI('https://www.baidu.com')
    obj.sendKeys('kw', 'python')
    time.sleep(3)