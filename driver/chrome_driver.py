#!/usr/bin/env python 3
# -*- coding:utf-8 -*-

from selenium import webdriver

class RunDriver(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_page(self, url):
        """
        :param url:the post url
        :return:
        """
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(url)
        return self.driver

    def close_driver(self):
        self.driver.close()
        self.driver.quit()
