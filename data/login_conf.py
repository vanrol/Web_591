# !/usr/env python 3
# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
import config.conf as config

# 賬號數據
usr_info = {
    '正確賬號': '0921000001',
    '錯誤賬號': '09210000001',
    '賬號滲透': "admin' OR 1=1/*",
    '空格賬號': " "
}

# 密碼數據
pwd_info = {
    '正確密碼': '111111',
    '錯誤密碼': '1111111',
    '密碼滲透': "1'or'1'='1",
    '空格密碼': " "
}


@pytest.fixture(scope='session', autouse=True)
def browser():
    global driver
    driver = config.driver
    driver.maximize_window()
    driver.implicitly_wait(20)
    driver.get('https://www.debug.591.com.tw/user-login.html')
    return driver

@pytest.fixture(scope="session", autouse=True)
def browser_close():
    yield driver
    driver.quit()

