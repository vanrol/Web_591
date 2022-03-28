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

    def login(self, usr, pwd, keep_cookie=False):
        '''
        :param usr:用戶名
        :param pwd:密碼
        :param keep_cookie:是否保持免登錄，默認不用
        :return:無返回
        '''
        self.usr_input.send_keys(usr)
        self.pwd_input.send_keys(pwd)
        # 如果需要保持登錄，則點擊保存後再點【登錄】。否則直接點擊【登錄】
        if keep_cookie:
            self.cookie_btn.click()
            self.login_btn.click()
        else:
            self.login_btn.click()
