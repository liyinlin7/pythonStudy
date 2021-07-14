#!D:\Python\Python39 python
# -*- coding: utf-8 -*-

import sys

#import readConfig
case_path = sys.path[0]
from Public.Utils import utils
import unittest
import datetime

#localReadConfig = readConfig.ReadConfig()


class TT(unittest.TestCase):
    '''舞单接口测试 2021-3-3'''

    @classmethod
    def setUpClass(cls):
        cls.ai = "/ai"
        cls.nowtime = datetime.datetime.strftime(datetime.datetime.now(), '%m%d%H%M%S')
        cls.createtime = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        cls.aftertime = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=3), '%Y-%m-%d')
        cls.startTime = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(seconds=10), '%H:%M:%S')
        cls.user = "18989848397"
        cls.Token = utils().getToken(username=cls.user)

    @classmethod
    def tearDownClass(cls):
        print('test end')

    def test_0101(self):
        '''查询个人主页-普通用户'''
        data = {"userId": self.userId}
        url_part = self.ai + "/usercertinfo/getUserInfo" + utils.parse_url(data)
        # result = utils().getRequest(url_part=url_part,Token=self.Token)
        # print(result)

    def test_0102(self):
        '''查询个人主页-UP用户'''
        data = {"userId":8426} #嗨动_9p1868
        url_part =self.ai + "/usercertinfo/getUserInfo"+utils.parse_url(data)
        result = utils().getRequest(url_part=url_part,Token=self.Token)

    # @unittest.skip("1")
    def test_02(self):
        '''修改个人信息'''
        data = {
                  "cover": "https://pub.hidbb.com/ai-dev/ai/27191b9870f04842a7513805d934c0bc.png",
                  "nickName": "2021",
                  "sex":'0'

                }
        url_part =self.ai + "/hidouserinfo/editInfo"
        utils().postRequest(url_part=url_part,Content_type="json",data=data,Token=self.Token)
        TT().test_0101()

    @unittest.skip("1")
    def test_03(self):
        '''新增动态'''
        data = {
                  "content": "发动态啦，现在是北京时间："+str(self.createtime),
                  "images": [
                  ]
                }
        url_part =self.ai + "/dynamic"
        utils().postRequest(url_part=url_part,Content_type="json",data=data,Token=self.Token)

    def test_04(self):
        '''动态列表'''
        url_part =self.ai + "/dynamic/list"
        result = utils().getRequest(url_part=url_part,Token=self.Token)




if __name__ == "__main__":
    unittest.main()
    # 流程说明

    # 流程结束
