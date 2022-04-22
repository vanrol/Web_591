# !/usr/env python 3
# -*- coding: utf-8 -*-
# Author:T5-10858 , Address:xuwanle@addcn.com

from page.mine_page import MinePage
from page.login_page import LoginPage
from data.login_data import *
from config.cfg import *
import allure
import time

# 登錄模塊測試用例
@allure.feature('登錄模塊')
class TestLogin(object):
    @allure.story("輸入错误賬號，错误密碼，登錄失敗，提示賬號錯誤。")
    @allure.severity(allure.severity_level.MINOR)
    def test_01(self, browser):
        global lg
        lg = LoginPage(browser)
        lg.login(usr_info['錯誤賬號'], pwd_info['錯誤密碼'])
        assert lg.warning_tip.text == lg.usr_warning

    @allure.story("輸入正確賬號，错误密碼，登錄失敗，提示密碼錯誤。")
    @allure.severity(allure.severity_level.NORMAL)
    def test_02(self):
        lg.login(usr_info['正確賬號'], pwd_info['錯誤密碼'])
        assert lg.warning_tip.text == lg.pwd_warning

    @allure.story("輸入正確賬號，正確密碼，登錄成功。")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_03(self):
        lg.login(usr_info['正確賬號'], pwd_info['正確密碼'])
        time.sleep(10)
        assert lg.get_url == MinePage.page_url

        # 對登錄成功跳轉頁面進行截圖
        pic_name = 'login_success' + time.strftime("%Y-%m-%d %H_%M_%S") + '.PNG'
        lg.screenshots(LOGS_PATH, pic_name)
        allure.attach.file(LOGS_PATH + '//' + pic_name, attachment_type=allure.attachment_type.PNG)

# if __name__ == '__main__':
#     pytest.main(["-v", "-s", "login_test.py", "--alluredir", report_path])
