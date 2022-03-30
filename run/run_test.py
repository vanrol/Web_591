# !/usr/env python 3
# -*- coding: utf-8 -*-
# Author:T5-10858 , Address:xuwanle@addcn.com

import config.cfg as cfg
import os

def run_main(file_name):
    # 執行目標用例
    f = cfg.testcase_path+'//'+file_name
    os.system("pytest {} -s -q --alluredir {}".format(f, cfg.report_path))
    # 保存測試報告，打開測試報告
    os.system("allure generate {} -o {} --clean".format(cfg.report_path, cfg.html_path))
    os.system("allure open {}".format(cfg.report_path + '//html'))

if __name__=='__main__':
    run_main('login_test.py')
