# !/usr/env python 3
# -*- coding: utf-8 -*-

import allure
import pytest
from common.page.login_page import LoginPage
from common.utils.chrome_driver import RunDriver
from data.login_conf import *

# 定義好用例的前置與後置條件，作用域：所有用例。前置條件：打開登錄頁面；後置條件：關閉頁面。
@pytest.fixture(scope='function', autouse=True)
def page_conf():
    global driver
    driver = RunDriver()
    url = LoginPage.page_url
    driver.open_page(url)
    yield
    driver.quit()

# 登錄模塊測試用例
@allure.feature('登錄模塊')
class TestLogin(object):
    @allure.story("輸入正確賬號密碼，登錄成功。")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_pass(self):
        with allure.step('1.輸入正確賬號{}；2.輸入正確密碼{}；3.點擊【登錄】按鈕。'.format(usr_info['正確賬號'],pwd_info['正確密碼'])):
            # LoginPage.usr_input.send_keys(user_info['正確賬號'])
            # LoginPage.pwd_input.send_keys(user_info['正確密碼'])
            # LoginPage.login_btn.click()
            LoginPage.login(usr_info['正確賬號'],pwd_info['正確密碼'])
            assert


