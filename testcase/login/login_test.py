# !/usr/env python 3
# -*- coding: utf-8 -*-
# Author:T5-10858 , Address:xuwanle@addcn.com

import time
from page.login_page import LoginPage
import allure
import pytest
from common.utils.read_yaml import read_yaml
from config.config import *

# 登錄模塊測試用例
@allure.feature('登錄模塊')
class TestLogin(object):
    # 标记用例等级为normal
    @allure.severity(allure.severity_level.NORMAL)
    # 读取key为normal的测试用例数据
    @pytest.mark.parametrize('login_data', read_yaml('login.yml', 'normal'))
    def test_fail(self, browser, login_data):
        # 实例化登录页面
        lg = LoginPage(browser)
        # 执行登录页面的登录功能
        lg.login(login_data['name'], login_data['psw'])
        # 获取执行登录操作后的页面元素，并与用例数据给出的期望结果进行断言
        assert lg.warning_tip.text == login_data['expect']
        # 将生成的报告标题改为用例标题
        allure.dynamic.title(login_data['title'])

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize('login_data', read_yaml('login.yml', 'critical'))
    def test_success(self, browser, login_data):
        lg = LoginPage(browser)
        lg.login(login_data['name'], login_data['psw'])
        time.sleep(8)
        assert lg.get_url == login_data['expect']
        allure.dynamic.title(login_data['title'])
        # 登陆成功后，进行截图操作
        pic_name = 'login_success' + time.strftime("%Y-%m-%d %H_%M_%S") + '.PNG'
        lg.screenshots(LOGS_PATH, pic_name)
        allure.attach.file(LOGS_PATH + '//' + pic_name, attachment_type=allure.attachment_type.PNG)

# if __name__ == '__main__':
#     pytest.main(["-v", "-s", "login_test.py", "--alluredir", report_path])
