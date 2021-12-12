#encoding utf-8
from selenium import webdriver
from time import sleep
from random import choice
from random import sample
import pymysql
import re

#创建一个公共类
class publicPhoneMethod():
    #构造方法
    def __init__(self,driver):
        self.driver=driver
    #配置测试环境方法
    def get_openProject(self):
        self.driver.get('http://test1www.comjia.com/project/s')
        sleep(1)
        self.driver.maximize_window()

    #创建随机手机号
    def createphone(self):
        mobilelist=['140','141','142']
        phone=choice(mobilelist)+''.join(choice('0123456789') for i in  range(8))
        return phone
        #mobilelist+从列表获取8个元素random.sample(list, 8)
        #phone = choice(mobilelist) + ''.join(sample(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], 8))

    #链接数据库获取验证码，对应注册
    def connsqlcaptcha(self,phone):
        #db = pymysql.connect("123.57.229.36", "comjia002_wukong", "affda33ac32", "comjia_merge", charset='utf8')
        db = pymysql.connect(host='123.57.229.36',
                             port=3306,
                             user='comjia002_wukong',
                              password='affda33ac32',
                             db='comjia_merge',
                             charset='utf8')
        cursor=db.cursor()
        cursor.execute("SELECT content  from cj_sms_log where phone=%s ORDER BY create_datetime desc limit 1", phone)
        data = str(cursor.fetchone())
        print('Database version : %s' % data)
        sleep(4)
        yzm=(''.join(list(filter(lambda x:x.isdigit(), data)))[0:4])
        ### 以下正则，获取验证码数字
        # yzm = re.findall(r'[0-9]+', data)
        # 已知两个数字，取第一个数字
        # yzm = yzm[0]
        # print(yzm)

        sleep(4)
        return yzm
        db.close()
        #关闭数据库
    #关联上yw_user_action_clue的订单,对应留电
    def connsql(self,phone,value):
        db = pymysql.connect(host='123.57.229.36',
                             port=3306,
                             user='comjia002_wukong',
                             password='affda33ac32',
                             db='comjia_merge',
                             charset='utf8')
        cursor =db.cursor()
        cursor.execute("SELECT id  from cj_user where mobile=%s ORDER BY create_datetime desc limit 1", phone)
        id = cursor.fetchone()
        print('Database version : %s' % id)
        sleep(3)
        cursor.execute(
            "SELECT create_datetime,op_type from yw_user_action_clue where creator=%s and op_type=%s ORDER BY create_datetime desc limit 1",
            (id, value))
        create_datetime, op_type = cursor.fetchone()
        print('Database version,time : %s,%s' % (op_type, create_datetime))
        db.close()
        return create_datetime,op_type


    #获取cj_user表的用户信息#
    def isregistert(self,phone):
        db = pymysql.connect(host='123.57.229.36',
                             port=3306,
                             user='comjia002_wukong',
                             password='affda33ac32',
                             db='comjia_merge',
                             charset='utf8')
        cursor = db.cursor()
        count=cursor.execute("select count(*) from cj_user where mobile=%s",phone)
        db.close()
        return count
    #获取当前url#
    def get_current_url(self):
        driver=self.driver
        url=driver.current_url
        return url



# #
# p=publicPhoneMethod(webdriver.Chrome())
# p.consql()
# p.isregister()
# p.geturl()





