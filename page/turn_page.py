# !/usr/env python 3
# -*- coding: utf-8 -*-

from poium import Page, Element, CSSElement

class TurnPage(Page):
    success_page_tip = Element(class_name='topInfoStyleWait', timeout=2, describe='跳轉頁面的提示')
    success_tip = '歡迎您的到來， 正在登入中。。。'