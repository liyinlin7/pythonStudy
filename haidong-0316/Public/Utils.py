#!D:\Python\Python39 python
# -*- coding: utf-8 -*-
'''
Project:工具类
'''
import json
import requests
import logging
import datetime, time, os
import warnings
import readConfig as readConfig
import warnings

localReadConfig = readConfig.ReadConfig()

#工具类
class utils:

    def __init__(self):
        '''初始加载参数，全局调用'''
        global Token
        self.host = localReadConfig.get_http("host")
        self.UserAgent = localReadConfig.get_http("UserAgent")
        self.userName = localReadConfig.get_http("userName")
        self.password = localReadConfig.get_http("password")
        self.phone = localReadConfig.get_http("phone")

    # 带？ dict 拼接url
    def parse_url(data={}):
        item = data.items()
        urls = "?"
        for i in item:
            (key, value) = i
            temp_str = key + "=" + str(value)
            urls = urls + temp_str + "&"
        urls = urls[:len(urls) - 1]
        return urls

    # 不带？ dict 拼接url
    def parse_urlparams(data={}):
        item = data.items()
        urls = ""
        for i in item:
            (key, value) = i
            temp_str = key + "=" + str(value)
            urls = urls + temp_str + "&"
        urls = urls[:len(urls) - 1]
        return urls

    # 确认返回结果的正确性,附带更多信息（补充url）
    def checkResp(response_passed, url):
        response_passed.encoding = 'utf-8'
        print(response_passed.text)
        response_passed.raise_for_status()
        result = json.loads(response_passed.text)
        if 'code' in result.keys():
            successOrFail = result['code']
            if str(successOrFail) == '0':
                logging.info(response_passed.text)
            else:
                raise response_passed.text

    def getRequest(self, url_part, params="", Token=""):
        '''GET请求+返回结果处理'''
        url = self.host + url_part
        print(url)
        requestData = ""
        if Token == "":
            self.headers = {'User-Agent': self.UserAgent}
        else:
            self.headers = {'User-Agent': self.UserAgent,
                            'Authorization': Token['token_type'] + ' ' + Token['access_token']}#
                            # 'Authorization': "Bearer 2b902420-c225-4fcf-acf9-2c3a09a5c4af"}#Token['token_type'] + ' ' + Token['access_token']
        # print(self.headers)
        if params == "":
            response_passed = requests.request("get", url, headers=self.headers, verify=False)
        else:
            response_passed = requests.request("get", url, params=params, headers=self.headers, verify=False)
        utils.checkResp(response_passed, url)
        data = json.loads(response_passed.text)['data']
        if data is not None:
            requestData = data
        return requestData

    def postRequest(self, url_part, Content_type="", data="", Token=""):
        '''POST请求+返回结果处理'''
        url = self.host + url_part
        requestData = ""
        if Token == "":
            self.headers = {'User-Agent': self.UserAgent}
            Jsonheaders = {'User-Agent': self.UserAgent,
                           'Content-type': "application/json;charset=UTF-8"}
        else:
            self.headers = {'User-Agent': self.UserAgent,
                            'Authorization': Token['token_type'] + ' ' + Token['access_token']}
            Jsonheaders = {'User-Agent': self.UserAgent,
                           'Authorization': Token['token_type'] + ' ' + Token['access_token'],
                           # 'Authorization': "Bearer 2b902420-c225-4fcf-acf9-2c3a09a5c4af",#Token['token_type'] + ' ' + Token['access_token']
                           'Content-type': "application/json;charset=UTF-8"}
            # print(Jsonheaders)
        if data == "":
            if Content_type == "json":
                response_passed = requests.request("post", url, headers=Jsonheaders)#, verify=False
            else:
                response_passed = requests.request("post", url, headers=self.headers)
        else:
            if Content_type == "json":
                response_passed = requests.request("post", url, data=json.dumps(data), headers=Jsonheaders)
            else:
                response_passed = requests.request("post", url, data=data, headers=self.headers, verify=False)
        print(url)
        utils.checkResp(response_passed, url)
        data = json.loads(response_passed.text)['data']
        if data is not None:
            requestData = data
        return requestData

    def putOrDelRequest(self, option="", url_part="", Content_type="", data="", Token=""):
        '''PUT/DELETE请求+返回结果处理'''
        url = self.host + url_part
        requestData = ""
        self.headers = {'User-Agent': self.UserAgent,
                        'Authorization': Token['token_type'] + ' ' + Token['access_token']}
        Jsonheaders = {'User-Agent': self.UserAgent,
                       'Authorization': Token['token_type'] + ' ' + Token['access_token'],
                       'Content-type': "application/json;charset=UTF-8"}
        if option:
            optionForRequest = option
        if data == "":
            if Content_type == "json":
                response_passed = requests.request(optionForRequest, url, headers=Jsonheaders)
            else:
                response_passed = requests.request(optionForRequest, url, headers=self.headers)
        else:
            if Content_type == "json":
                response_passed = requests.request(optionForRequest, url, data=json.dumps(data), headers=Jsonheaders)
            else:
                response_passed = requests.request(optionForRequest, url, data=data, headers=self.headers)
        utils.checkResp(response_passed, url)
        data = json.loads(response_passed.text)['data']
        if data is not None:
            requestData = data
        return requestData

    def postRequestForExport(self, url_part, Content_type="", data="", Token=""):
        '''导出的GET请求+返回结果处理'''
        url = self.host + url_part
        requestData = ""
        self.headers = {'User-Agent': self.UserAgent,
                        'Authorization': Token['token_type'] + ' ' + Token['access_token']}
        Jsonheaders = {'User-Agent': self.UserAgent,
                       'Authorization': Token['token_type'] + ' ' + Token['access_token'],
                       'Content-type': "application/json;charset=UTF-8"}
        if data == "":
            if Content_type == "json":
                response_passed = requests.request("post", url, headers=Jsonheaders)
            else:
                response_passed = requests.request("post", url, headers=self.headers)
        else:
            if Content_type == "json":
                response_passed = requests.request("post", url, data=json.dumps(data), headers=Jsonheaders)
            else:
                response_passed = requests.request("post", url, data=data, headers=self.headers)
        if response_passed.status_code == 500:
            print(response_passed.text)
        else:
            Excel = response_passed.headers.get('Content-Disposition')
            ExcelMessage = Excel.split("=")
            name = ExcelMessage[-1]
            with open(name, "wb") as code:
                code.write(response_passed.content)
                print("下载生成成功：文件名为"+name)
        return requestData

    def getToken(self, username=""):
        '''获取登陆Token'''
        if username == '':
            username = self.userName
        self.headers = {
            # 'User-Agent': self.UserAgent,
            'Content-Type': 'application/x-www-form-urlencoded',#application/x-www-form-urlencoded
            'Authorization': 'Basic dGVzdDp0ZXN0'#Basic dGVzdDp0ZXN0 # cGFtaXI6cGFtaXI=
        }
        # phoneurl = "http://pamir-gateway:9999/admin/mobile/"+str(username)
        phoneurl = self.host+"/admin/mobile/"+str(username)
        # phoneMsg = requests.request("get", phoneurl, headers=self.headers)#, verify=False
        # phoneYZM = json.loads(phoneMsg.text)['msg']
        phoneYZM = str(username)[-4:]
        # url = "http://pamir-gateway:9999/auth/mobile/token/sms?mobile=SMS%40"+str(username)+"&code="+str(phoneYZM)+"&grant_type=mobile"
        url = self.host+"/auth/mobile/token/sms?mobile=SMS%40"+str(username)+"&code="+str(phoneYZM)+"&grant_type=mobile"
        response_passed = requests.request("post", url, headers=self.headers)#, verify=False
        utils.checkResp(response_passed, url)
        Token = json.loads(response_passed.text)
        # utils.getrefreshToken(host=self.host,refresh=Token)
        return Token

    def getRegisterYZM(self,username=""):
        '''获取手机验证码'''
        self.headers = {
            'User-Agent': self.UserAgent,
            # 'Content-Type': 'application/x-www-form-urlencoded',
            # 'Authorization': 'Basic dGVzdDp0ZXN0'
        }
        # phoneurl = "http://pamir-gateway:9999/admin/mobile/"+str(username)
        phoneurl = "http://192.168.204.123:9999/admin/mobile/sendRegist?mobile="+str(username)
        phoneMsg = requests.request("get", phoneurl, headers=self.headers)
        phoneYZM = json.loads(phoneMsg.text)['msg']
        return phoneYZM

    def getOtherToken(self, url):
        '''获取第三方Token'''
        self.headers = {
            'User-Agent' : self.UserAgent
        }
        response_passed = requests.request("POST", url,headers=self.headers)
        utils.checkResp(response_passed, url)
        Token = json.loads(response_passed.text)
        print(Token)
        return Token
    #
    # def connHive(sql):
    #     '''Hive查询'''
    #     warnings.simplefilter("ignore", ResourceWarning)
    #     conn = ipdb.connect(host='10.18.70.102', port=10000, user='hdfs', auth_mechanism='PLAIN')
    #     # 使用cursor()方法获取操作游标
    #     cursor = conn.cursor()
    #     # 异常处理
    #     HiveRequest = ""
    #     try:
    #         cursor.execute(sql)
    #         HiveRequest = cursor.fetchall()
    #     except Exception as e:
    #         # hive不支持事务
    #         raise e
    #     finally:
    #         cursor.close()
    #         # 关闭数据库连接
    #         conn.close()
    #     return HiveRequest

#时间公用方法
    #等待时间计算
    def timing(self, waitTime):
        minute = datetime.datetime.now().strftime('%M')
        remainder = int(minute)%int(waitTime)
        if remainder == 0:
            time.sleep(waitTime*60)#等待五分钟
        elif 0 < remainder < waitTime:
            sleepTime = int(waitTime) - remainder
            time.sleep(sleepTime*60)

    def get_1st_of_last_month(self):
        """
        获取上个月第一天的日期，然后加21天就是22号的日期
        :return: 返回日期
        """
        today = datetime.datetime.today()
        year = today.year
        month = today.month
        if month == 1:
            month = 12
            year -= 1
        else:
            month -= 1
        res = datetime.datetime(year, month, 1) + datetime.timedelta(days=21)
        res = res.strftime("%Y%m%d")
        return res

    def get_1st_of_next_month(self):
        """
        获取下个月的22号的日期
        :return: 返回日期
        """
        today = datetime.datetime.today()
        year = today.year
        month = today.month
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
        res = datetime.datetime(year, month, 1) + datetime.timedelta(days=21)
        return res

    def getYesterday(self):
        """
        获取昨天
        """
        today=datetime.date.today()
        oneday=datetime.timedelta(days=1)
        yesterday=today-oneday
        yesterday = yesterday.strftime("%Y%m%d")
        return yesterday

    def getYesterday_ymd(self):
        """
        180303
        """
        today=datetime.date.today()
        oneday=datetime.timedelta(days=1)
        yesterday=today-oneday
        yesterday = yesterday.strftime("%y%m%d")
        return yesterday

    def getDict(self, type="", Token=""):
        '''获取项目字典项信息'''
        url = "http://pamir-gateway:9999/admin/dict/type/"+type
        self.headers = {
            'User-Agent' : self.UserAgent,
            'Authorization': Token['token_type'] + ' ' + Token['access_token']
        }
        response_passed = requests.request("get", url, headers=self.headers)
        utils.checkResp(response_passed, url)
        Dict = json.loads(response_passed.text)['data']
        return Dict


    def postRequestKK(self, url_part, Content_type="", data="", Token=""):
        '''POST请求+返回结果处理'''
        url = url_part
        requestData = ""
        self.headers = {'User-Agent': self.UserAgent,
                        'Authorization': 'Bearer' + ' ' + Token['access_token']
                        }
        Jsonheaders = {'User-Agent': self.UserAgent,
                       'Authorization': 'Bearer' + ' ' +Token['access_token'],
                       'Content-type': 'application/json;charset=UTF-8'}
        print(Token)
        if data == "":
            if Content_type == "json":
                response_passed = requests.request("post", url, headers=Jsonheaders)
            else:
                response_passed = requests.request("post", url, headers=self.headers)
        else:
            if Content_type == "json":
                response_passed = requests.request("post", url, data=json.dumps(data), headers=Jsonheaders)
            else:
                response_passed = requests.request("post", url, data=data, headers=self.headers)
        utils.checkResp(response_passed, url)
        data = json.loads(response_passed.text)['data']
        if data is not None:
            requestData = data
        return requestData

    def getNow(self):
        '''获取当前时间'''
        time = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S')
        return time

    def getAppointTime(self, days):
        '''获取指定时间'''
        time = datetime.datetime.strftime(datetime.datetime.now() - datetime.timedelta(days=days), '%Y-%m-%d %H:%M:%S')
        return time

    def uploadByPost(self, url_part="",Token=""):
        '''文件上传'''
        url = self.host + url_part
        files = {'multipartFile':open('E:\workSpace\haidong\TestSuite_tjj\TestCase\Manage\phone.txt','rb')}
        self.headers = {'User-Agent': self.UserAgent,
                        'Authorization': 'Bearer' + ' ' + Token['access_token'],
                        }
        response_passed = requests.request("post", url, files=files,headers=self.headers)
        utils.checkResp(response_passed, url)
        data = json.loads(response_passed.text)['data']
        if data is not None:
            requestData = data
        return requestData

    def uploadGIFByPost(self, url_part="",Token=""):
        '''文件图片/视频'''
        url = self.host + url_part
        file_path = "E:\workSpace\haidong\TestSuite_tjj\image\m1.jpg"
        file = {"file":("m1.jpg", open(file_path, 'rb'),'image/jpeg',{})}
        headers_from_data = {'User-Agent': self.UserAgent,
                             'Authorization': 'Bearer' + ' ' + Token['access_token']#,
                             # 'Content-Type':'multipart/form-data'
                             }
        response_passed = requests.request("POST",url, headers=headers_from_data, files=file)
        # warnings.simplefilter("ignore", ResourceWarning)
        utils.checkResp(response_passed, url)

        fileUrl = json.loads(response_passed.text)['data']['fileUrl']
        return fileUrl

    def getFileList(self):
        # file_dir = "E:\workSpace\haidong\TestSuite_tjj\TestCase\AI\_timing"
        # file_dir = "E:\workSpace\haidong\TestSuite_tjj\TestCase\AI\_tigger"
        # file_dir = "E:\workSpace\haidong\TestSuite_tjj\TestCase\AI\_image"
        file_dir = "E:\workSpace\haidong\TestSuite_tjj\TestCase\AI\_keys"
        path_list = os.listdir(file_dir)
        # path_list.remove('.DS_Store')
        path_list.sort(key=lambda x:int(x.split('.')[0]))
        print(path_list)
        # fileList = ""
        # for files in os.walk(file_dir):
        #     print(files)  # 当前路径下所有非目录子文件
        #     fileList = files[2]
        return path_list


    def uploadMp3ByPost(self, url_part="",filename='',Token=""):
        '''上传音频'''
        url = self.host + url_part
        # file_path = "E:\workSpace\haidong\TestSuite_tjj\TestCase\AI\_timing"+"/"+filename
        file_path = "E:\workSpace\haidong\TestSuite_tjj\TestCase\AI\_tigger"+"/"+filename
        mp3Open = open(file_path, 'rb')
        file = {"multipartFile":(filename+".mp3",mp3Open,'audio/mp3',{})}
        headers_from_data = {'User-Agent': self.UserAgent,
                             'Authorization': 'Bearer' + ' ' + Token['access_token']#,
                             # 'Content-Type':'multipart/form-data'
                             }
        response_passed = requests.request("POST",url, headers=headers_from_data, files=file)
        utils.checkResp(response_passed, url)
        fileInfo = json.loads(response_passed.text)['data']
        mp3Open.close()
        return fileInfo


    def uploadJPGByPost(self, url_part="",filename='',Token=""):
        '''文件图片/视频'''
        url = self.host + url_part
        # file_path = "E:\workSpace\haidong\TestSuite_tjj\TestCase\AI\_image"+"/"+filename
        file_path = "E:\workSpace\haidong\TestSuite_tjj\TestCase\AI\_keys"+"/"+filename
        jpgFile = open(file_path, 'rb')
        file = {"file":("m1.jpg", jpgFile,'image/jpeg',{})}
        headers_from_data = {'User-Agent': self.UserAgent,
                             'Authorization': 'Bearer' + ' ' + Token['access_token']#,
                             # 'Content-Type':'multipart/form-data'
                             }
        response_passed = requests.request("POST",url, headers=headers_from_data, files=file)
        # warnings.simplefilter("ignore", ResourceWarning)
        utils.checkResp(response_passed, url)
        jpgFile.close()
        fileUrl = json.loads(response_passed.text)['data']
        print(fileUrl)
        return fileUrl

    def getrefreshToken(host="",refresh=""):
        print(3)
        data = {
            "grant_type": "refresh_token",
            "refresh_token": refresh['refresh_token'],
            "client_id": "pamir",
            "client_secret": "pamir"
        }
        url = host+"/auth/oauth/token"+utils.parse_url(data)
        # headers = {
            # 'User-Agent': self.UserAgent,
        #     'Content-Type': 'application/json'#,
        #     # 'Authorization': 'Basic dGVzdDp0ZXN0'
        # }
        response_passed = requests.request("get", url)#, headers=headers
        utils.checkResp(response_passed, url)
        rToken = json.loads(response_passed.text)
        return rToken