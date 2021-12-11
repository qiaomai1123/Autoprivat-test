#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pycharm-test 
@File ：test_xpath.py
@IDE  ：PyCharm 
@Author ：qiaochunwei
@Date ：2021/12/4 0:19 
'''
import time
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from testcase.public import testbase
from methond.public_testapi import public_testapi

test_url=public_testapi().get_url(1,'pc')
test_msg=public_testapi().get_msg(1,'pc')

@ddt
class Case01(testbase):
    '''测试用例练习'''
    # def test_case01(self):
    #     try:
    #         self.driver.get('http://test1www.comjia.com/project/s')
    #         time.sleep(1)
    #         self.driver.execute_script('window.scrollTo(0,500)')
    #         time.sleep(2)
    #         self.driver.find_element_by_xpath("//div[@class='customer-info']/a[@class='btn1-v5 btn-blue-border new_common_free_btn']").click()
    #         time.sleep(2)
    #         self.driver.find_element_by_xpath("//div[@class='dialog dialog-consultant dialog-cons-horizontal layui-layer-wrap']//div/input").send_keys('17788887777')
    #         time.sleep(2)
    #         self.driver.find_element_by_xpath("//div[@class='layui-layer layui-anim layui-layer-page ']//button[@class='btn btn3 new_common_free_submit']").click()
    #         time.sleep(2)
    #         self.driver.find_element_by_xpath("//div[@class='layui-layer-content  dialog dialog-yuyue-success layui-layer-wrap']//button").click()
    #         time.sleep(2)
    #         self.driver.find_element_by_xpath("//div[@class='layui-layer-content submit-need second-submit-success layui-layer-wrap']//button").click()
    #         time.sleep(1)
    #     except Exception as e:
    #         print(e)
    #         self.add_img()
    #         raise
    # def test_case02(self):
    #     self.driver.get('http://test1www.comjia.com/project/s')
    #     time.sleep(1)
    #     self.driver.execute_script('window.scrollTo(0,500)')
    #     time.sleep(1)
    #     self.img = []
    #     self.img.append(self.driver.get_screenshot_as_base64())
    #     index1 = self.driver.current_window_handle
    #     self.driver.find_element_by_xpath("//div[@class='des-title']").click()
    #     time.sleep(1)
    #     self.driver.switch_to.window(index1)
    #     time.sleep(1)
    #     self.driver.window_handles
    #     self.driver.switch_to.window(self.driver.window_handles[1])
    #     time.sleep(1)
    # @data('测试面试题')
    # @data(['测试面试题'],['自动化面试题']) #一个参数两遍执行
    @data(['测试','方法']) #两个参数 一个列表一对
    # @data(*public_test().read_file())
    @unpack
    def test_case03(self, username, pwd):
        ''''百度搜索'''
        try:
            msg = test_msg[0]
            self.driver.get(test_url[0])
            time.sleep(2)
            self.driver.find_element_by_id('kw').send_keys(username)
            time.sleep(1)
            self.driver.find_element_by_id('kw').clear()
            time.sleep(1)
            self.driver.find_element_by_id('kw').send_keys(pwd)
            time.sleep(1)
            self.driver.find_element_by_xpath("//span[@class='bg s_btn_wr']").click()
            time.sleep(1)
            title = self.driver.find_element_by_xpath("//a[@class='toindex']").text
            self.add_img()
            self.assertEqual(title, msg)
        except Exception as e:
            print(e)
            self.add_img()
            raise







