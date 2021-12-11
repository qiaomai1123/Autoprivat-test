import os
import yaml


class Readwhriteyaml:
    #读取
    def read_extract_yaml(self,key):
        with open(os.getcwd()+"/yam.yml", mode='r', encoding='utf-8')as f:
            value=yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]
    #存储
    def write_extract_yaml(self,data):
        with open(os.getcwd()+"/yam.yml", mode='a', encoding='utf-8')as f:#a追加#w覆盖
            yaml.dump(data=data, stream=f, allow_unicode=True)
    #追加#w覆盖
    def clear_extract_yaml(self):
        with open(os.getcwd()+"/yam.yml", mode='w', encoding='utf-8')as f:#a追加#w覆盖
            f.truncate()
    #读取测试用例yml的数据
    def read_testcase_yaml(self,yml_name):
        with open("./testcase/"+yml_name, mode='r', encoding='utf-8')as f:
            value=yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

