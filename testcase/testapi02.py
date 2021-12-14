#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pycharm-test 
@File ：testapi02.py
@IDE  ：PyCharm 
@Author ：qiaochunwei
@Date ：2021/12/14 14:45 
'''
import unittest
from ddt import ddt,data,unpack
import requests
@ddt
class testapi02(unittest.TestCase):

    def test_ws02(self):
        url = 'http://toutiao-app.itheima.net/v1_0/search'
        data = {
            "page": 1,
            "per_page": 12,
            "q": "测试"
        }
        headers = 'application/json'
        try:
            res = requests.get(url=url, data=data)
            print(res.text)
        except Exception as e:
            print(e)


