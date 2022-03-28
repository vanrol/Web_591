# !/usr/env python 3
# -*- coding: utf-8 -*-

from poium import Page, Element, CSSElement

class MinePage(Page):
    page_url = 'https://www.debug.591.com.tw/index.php?module=userCenter&action=newMedium'
    first_tab = CSSElement('.first select')