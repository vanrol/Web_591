# !/usr/env python 3
# -*- coding: utf-8 -*-
import time
from poium import Page, Element
from config.cfg import *

class LoginPage(Page):
    # 頁面基本按鈕控件
    page_url = 'https://www.debug.591.com.tw/user-login.html'
    usr_input = Element(name='user.username', describe='賬號輸入框')
    pwd_input = Element(name='user.pwd', describe='密碼輸入框')
    found_usr = Element(link_text='忘記帳號', describe='忘記賬號按鈕')
    found_pwd = Element(link_text='忘記密碼', describe='忘記密碼按鈕')
    cookie_btn = Element(class_name='j-cookie', describe='兩周內免登錄勾選按鈕')
    login_btn = Element(id_='login_sub', describe='登入按鈕')
    register_btn = Element(link_text='免費註冊', describe='免費註冊')
    warning_tip = Element(class_name='login-warning-info', describe='登录提示')
    success_page_tip = Element(class_name='topInfoStyleWait', describe='跳轉頁面的提示')

    # 頁面相關提示
    usr_warning = '您輸入的帳號不存在'
    pwd_warning = '您輸入的密碼有誤，請重新輸入。忘記密碼？'
    success_tip = '歡迎您的到來， 正在登入中。。。'



def login(driver, usr, pwd, keep_cookie=False):
    '''
    :param usr:用戶名
    :param pwd:密碼
    :param keep_cookie:是否保持免登錄，默認不用
    :return:無返回
     '''
    lp = LoginPage(driver)
    lp.usr_input.send_keys(usr)
    lp.pwd_input.send_keys(pwd)
    if keep_cookie:
        lp.cookie_btn.click()
        lp.login_btn.click()
    else:
        lp.login_btn.click()
