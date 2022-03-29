# !/usr/env python 3
# -*- coding: utf-8 -*-
# Author:T5-10858 , Address:xuwanle@addcn.com

import pytest
import config.cfg as cfg
from common.page.login_page import LoginPage

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



# 登錄測試類前後置：驅動開啟與關閉
@pytest.fixture(scope='class', autouse=True)
def browser():
    # 前置：打開登錄頁並進行頁面大小調整
    driver = cfg.driver_tool
    driver.maximize_window()
    driver.implicitly_wait(20)
    lp = LoginPage(driver)
    lp.open(lp.page_url)

    yield driver  # 返回驅動，供外部調用
    # 後置：關閉瀏覽器
    driver.quit()

# 登錄測試用例前後置工作：清除輸入框
@pytest.fixture(scope='function', autouse=True)
def clear():
    driver = cfg.driver_tool
    lp = LoginPage(driver)
    lp.usr_input.clear()
    lp.pwd_input.clear()

