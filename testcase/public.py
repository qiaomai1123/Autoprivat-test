#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pycharm-test 
@File ：public.py.py
@IDE  ：PyCharm 
@Author ：qiaochunwei
@Date ：2021/12/9 0:25 
'''
from selenium import webdriver
import unittest

class testbase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.imgs = []

    def add_img(self):
        self.imgs.append(self.driver.get_screenshot_as_base64())

    def tearDown(self):
        self.driver.delete_all_cookies()
        pass