#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pycharm-test 
@File ：runtestapi01.py
@IDE  ：PyCharm 
@Author ：qiaochunwei
@Date ：2021/12/12 22:21 
'''
import unittest
import HTMLTestReportCN

if __name__=='__main__':
    suite = unittest.defaultTestLoader.discover(start_dir='./testcase/', pattern='testapi*.py')
    fp=open('./report/test_reportapi01.html', 'wb')
    runner=HTMLTestReportCN.HTMLTestRunner(stream=fp, title='xml测试报告',verbosity=1)
    runner.run(suite)
    fp.close()