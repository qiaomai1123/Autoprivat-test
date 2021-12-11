import json
import re

import pytest
import requests
# requests.get()
# requests.post()
# requests.delete()
# requests.put()
# requests.request()
from methond.yamtest import Readwhriteyaml




class Testpost:
    @pytest.fixture(scope="session",autouse=True)
    def clear_yaml(self):
        Readwhriteyaml().clear_extract_yaml()
    # def setup(self):
    #     print('每一次用例前执行')
    # def teardown(self):
    #     print('每一次用例后执行')
    @pytest.mark.parametrize('caseinfo',Readwhriteyaml().read_testcase_yaml('get_data.yml'))
    def test_1get(self, caseinfo):
        url= caseinfo['request']['url']
        data=caseinfo['request']['data']
        keywords= caseinfo['request']['data']['keywords']
        print(keywords)
        repget=requests.get(url, params=data)
        print(repget.text)
        if keywords != None:
            assert keywords in repget.text
        else:
            print("keywords为空")
            assert '参数错误' in repget.text
        # name = re.search('"id":298317,"name":"(.*?)"', repget.text)[1]
        # print(name)
        # Readwhriteyaml().write_extract_yaml({'name':name})
        # if
        # assert '参数错误' not in repget.text
    #
    # def test_2post(self):
    #     value = Readwhriteyaml().read_extract_yaml('name')
    #     url = "https://testapiclient.comjia.com/icsoc/call-after"
    #     data={
    #          "type": 1,
    #          "data": {
    #                 "callid": "6831526890717581312",
    #                 "vcc_code": "6018051501",
    #                 "server_num": "01083621045",
    #                 "cus_phone": "13670265008",
    #                 "cus_phone_areacode": "0755",
    #                 "cus_phone_areaname": "广东 深圳",
    #                 "cus_phone_type": "MOBILE",
    #                 "ag_name": value,
    #                 "ag_num": "2091",
    #                 "ag_phone": "8371",
    #                 "ag_phone_areacode": "",
    #                 "ag_phone_areaname": "",
    #                 "ag_phone_type": "SIP",
    #                 "ag_conn_time": "1628762934",
    #                 "cus_conn_time": "0",
    #                 "end_time": "1628762945",
    #                 "ring_secs": "9",
    #                 "conn_secs": "0",
    #                 "all_secs": "11",
    #                 "result": "IVR挂机",
    #                 "result_code": "1",
    #                 "record_url": "",
    #                 "endResult": "振铃放弃",
    #                 "endResult_code": "1",
    #                 "call_type": "1",
    #                 "user_data": {},
    #                 "user_sipcode": "487",
    #                 "user_pricode": "16",
    #                 "ring_time": "1628762936"
    #                 }
    #         }
    #     # rep = requests.post(url, json=data)
    #     rep1=requests.post(url, data=json.dumps(data))  #字典格式转成str格式
    #     print(rep1.json())
    #     assert 'ok' in rep1.text














# # 可写函数说明
# def changeme(mylist):
#     "修改传入的列表"
#     mylist.append([1, 2, 3, 4])
#     print("函数内取值: ", mylist)
#     return
#
#
# # 调用changeme函数
# mylist = [10, 20, 30]
# changeme(mylist)
# print("函数外取值: ", mylist)