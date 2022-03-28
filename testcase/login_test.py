# !/usr/env python 3
# -*- coding: utf-8 -*-

from poium import Page, Element
from data.login_conf import *
import config.conf as config
import allure
import pytest
from common.page.login_page import login, LoginPage as lp
from common.page.mine_page import MinePage
from data.login_conf import *
import config.conf as conf
from common.utils.driver import RunDriver


# 登錄模塊測試用例
@allure.feature('登錄模塊')
class TestLogin(object):
    def setup_method(self):
        self.driver = RunDriver()
        self.driver.open_page(lp.page_url)

    def teardown_method(self):
        self.driver.close()

    @allure.story("輸入正確賬號密碼，登錄成功。")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self):
        with allure.step('1.輸入正確賬號{}；2.輸入正確密碼{}；3.點擊【登錄】按鈕。'.format(usr_info['正確賬號'], pwd_info['正確密碼'])):
            login(self.driver, usr_info['正確賬號'], pwd_info['正確密碼'])
            assert MinePage.first_tab == True

    @allure.story("輸入错误賬號错误密碼，登錄成功。")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login1(self):
        with allure.step('1.輸入错误賬號{}；2.輸入错误密碼{}；3.點擊【登錄】按鈕。'.format(usr_info['錯誤賬號'], pwd_info['错误密碼'])):
            login(self.driver, usr_info['错误賬號'], pwd_info['错误密碼'])
            assert lp.login_tip  == '您輸入的密碼有誤，請重新輸入。忘記密碼？'
