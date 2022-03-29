# !/usr/env python 3
# -*- coding: utf-8 -*-
# Author:T5-10858 , Address:xuwanle@addcn.com

import allure
from common.page.login_page import login
from config.login_cfg import *
from data.login_data import *


# 登錄模塊測試用例
@allure.feature('登錄模塊')
class TestLogin(object):

    @allure.story("輸入错误賬號错误密碼，登錄失敗，提示賬號錯誤。")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_01(self, browser):
        with allure.step('1.輸入错误賬號{}；2.輸入错误密碼{}；3.點擊【登錄】按鈕。'.format(usr_info['錯誤賬號'], pwd_info['錯誤密碼'])):
            login(browser, usr_info['錯誤賬號'], pwd_info['錯誤密碼'])
            lg = LoginPage(browser)
            assert lg.warning_tip.text == LoginPage.usr_warning

    @allure.story("輸入正確賬號错误密碼，登錄失敗，提示密碼錯誤。")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_02(self, browser):
        with allure.step('1.輸入错误賬號{}；2.輸入错误密碼{}；3.點擊【登錄】按鈕。'.format(usr_info['正確賬號'], pwd_info['錯誤密碼'])):
            login(browser, usr_info['正確賬號'], pwd_info['錯誤密碼'])
            lg = LoginPage(browser)
            assert lg.warning_tip.text == LoginPage.pwd_warning


if __name__ == '__main__':
    pytest.main(["-v", "-s", "login_test.py"])
