# 此模块主要存放框架中所有目录的绝对路径
import os


# 获取项目根目录
BASE_PATH = os.path.dirname(os.path.dirname(__file__))
# 获取各个包的绝对路径
LOGS_PATH = os.path.join(BASE_PATH, 'logs')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
HTML_PATH = os.path.join(REPORT_PATH, 'html')
DATA_PATH = os.path.join(BASE_PATH, 'data')
TESTCASE_PATH = os.path.join(BASE_PATH, 'testcase')



