#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：pycharm-test
@File ：test_post.py
@IDE  ：PyCharm
@Author ：qiaochunwei
@Date ：2021/11/30 19:44
'''
import json
import os
import re
import yaml

import pytest
import requests

from methond.yamtest import Readwhriteyaml


class Testapi1:
    @pytest.mark.parametrize('info', Readwhriteyaml().read_testcase_yaml('test_case.yml'))
    def test_case1(self, info):
        print(info)
        method = info['api_request']['method']
        url = info['api_request']['url']
        req = info['api_request']['data']
        headers = info['api_request']['headers']
        eql = info['assert']['eq']
        result = requests.post(url, json=req, headers= headers)
        print(result.status_code)
        print(result.json())
        assert eql['code'] == result.json()['code']




