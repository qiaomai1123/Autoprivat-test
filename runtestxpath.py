#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pycharm-test 
@File ：runtestxpath.py
@IDE  ：PyCharm 
@Author ：qiaochunwei
@Date ：2021/12/4 22:28 
'''
import unittest
from testcase.test_xpath import Case01
import HTMLTestReportCN

if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(Case01('test_case03'))
    # unittest.TextTestRunner().run(suite)
    suite = unittest.defaultTestLoader.discover(start_dir='./testcase/', pattern='test_x*.py')
    # unittest.TextTestRunner().run(suite)
    fp = open('./report/test_report.html', 'wb')
    runner= HTMLTestReportCN.HTMLTestRunner(stream=fp, title='百度测试报告', verbosity=1)
    runner.run(suite)
    fp.close()