# !/usr/env python 3
# -*- coding: utf-8 -*-
# Author:T5-10858 , Address:xuwanle@addcn.com

import time
from page.login_page import LoginPage
import allure
import pytest
from common.utils.read_yaml import read_yaml

# 登錄模塊測試用例
@allure.feature('登錄模塊')
class TestLogin(object):
    # 标记用例等级为normal
    @allure.severity(allure.severity_level.NORMAL)
    # 读取key为normal的测试用例数据
    @pytest.mark.parametrize('login_data', read_yaml('login.yml', 'normal'))
    def test_normal(self, browser, login_data):
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
    def test_critical(self, browser, login_data):
        lg = LoginPage(browser)
        lg.login(login_data['name'], login_data['psw'])
        time.sleep(8)
        assert lg.get_url == login_data['expect']
        allure.dynamic.title(login_data['title'])

# if __name__ == '__main__':
#     pytest.main(["-v", "-s", "login_test.py", "--alluredir", report_path])
