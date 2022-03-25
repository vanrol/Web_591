# !/usr/env python 3
# -*- coding: utf-8 -*-

from poium import Page, Element
class LoginPage(Page):
    page_url = 'https://www.debug.591.com.tw/user-login.html'
    usr_input = Element(name='user.username', describe='賬號輸入框')
    pwd_input = Element(name='user.pwd', describe='密碼輸入框')
    found_usr = Element(link_text='忘記帳號', describe='忘記賬號按鈕')
    found_pwd = Element(link_text='忘記密碼', describe='忘記密碼按鈕')
    cookie_btn = Element(id='cookie', describe='兩周內免登錄勾選按鈕')
    login_btn = Element(id='login_sub', describe='登入按鈕')
    register_btn = Element(link_text='免費註冊', describe='免費註冊')

