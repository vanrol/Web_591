# !/usr/env python 3
# -*- coding: utf-8 -*-
# Author:T5-10858 , Address:xuwanle@addcn.com

# !/usr/env python 3
# -*- coding: utf-8 -*-
# Author:T5-10858 , Address:xuwanle@addcn.com

import config.config as cfg
import os


def run_main(moudle_name, file_name):
    """
    :param moudle_name:tesecase文件下的模塊名稱
    :param file_name: 該模塊名稱下的py文件名
    :return: 無
    """
    # 執行目標用例
    MOUDLE_PATH = os.path.join(cfg.TESTCASE_PATH, moudle_name)
    f = os.path.join(MOUDLE_PATH, file_name)
    os.system("pytest {} -s -q --alluredir {}".format(f, cfg.REPORT_PATH))
    # 保存測試報告，打開測試報告
    os.system("allure generate {} -c -o {}".format(cfg.REPORT_PATH, cfg.HTML_PATH))
    os.system("allure open {}".format(cfg.HTML_PATH))


if __name__ == '__main__':
    run_main('login', 'login_test.py')
