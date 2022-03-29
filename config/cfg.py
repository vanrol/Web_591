# 此模块主要存放框架中所有目录的绝对路径
import os
from selenium import webdriver

# 获取项目根目录
root_path = os.path.dirname(os.path.dirname(__file__))
# 获取各个包的绝对路径
logs_path = root_path + '//' + 'logs'
page_path = root_path + '//' + 'common' + '//' + 'page'
utils_path = root_path + '//' + 'common' + '//' + 'utils'
report_path = root_path + '//' + 'report'
driver_path = root_path + '//' + 'driver'
data_path = root_path + '//' + 'data'
testcase_path = root_path + '//' + 'testcase'

# 浏览器设置
driver_tool = webdriver.Firefox()
