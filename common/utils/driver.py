#!/usr/bin/env python 3
# -*- coding:utf-8 -*-
# Author:T5-10858 , Address:xuwanle@addcn.com

from selenium import webdriver
import config.config as conf

class RunDriver(object):
    def __init__(self):
        self.driver = conf.driver_tool

    def open_page(self, url):
        """
        :param url:the post url
        :return:
        """
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        self.driver.get(url)
        return self.driver

    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()
