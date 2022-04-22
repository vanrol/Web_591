# !/usr/env python 3
# -*- coding: utf-8 -*-
# Author:T5-10858 , Address:xuwanle@addcn.com

import pytest
import config.cfg as cfg
from page.login_page import LoginPage


# 登錄測試類前後置：驅動開啟與關閉
@pytest.fixture(scope='class', autouse=True)
def browser():
    # 前置：打開登錄頁並進行頁面大小調整
    global driver
    driver = cfg.Driver
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
    lp = LoginPage(driver)
    lp.usr_input.clear()
    lp.pwd_input.clear()


