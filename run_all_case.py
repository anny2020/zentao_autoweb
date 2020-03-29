# @Time: 2020/3/22  18:04
import unittest
from common.HTMLTestRunner_cn import HTMLTestRunner

case_path = r"E:\PycharmProjects\100days\autoweb\case"
rule = "test*.py"
discover = unittest.defaultTestLoader.discover(start_dir=case_path,pattern=rule)
print(discover)

report_path = r"E:\PycharmProjects\100days\autoweb\report"+".html"
fp = open(report_path,'wb')

runner = HTMLTestRunner(stream=fp,title='报告名称',description='描述')
runner.run(discover)
fp.close()