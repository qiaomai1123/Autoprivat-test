#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pycharm-test 
@File ：testapi01.py
@IDE  ：PyCharm 
@Author ：qiaochunwei
@Date ：2021/12/10 17:22 
'''
import requests
import pytest
from xml.etree.ElementTree import ElementTree as EL
from xml.etree.ElementTree import fromstring
url='http://ws.webxml.com.cn/WebServices/WeatherWS.asmx/getRegionProvince'
res = requests.get(url=url)
print(res.status_code)
print(res.text)
doc=fromstring(res.text)
print(doc.find('./{http://WebXml.com.cn/}string').text)
print(len(doc.findall('./{http://WebXml.com.cn/}string'))) #string数量