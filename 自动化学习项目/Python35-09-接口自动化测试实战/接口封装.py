import json
import requests
import logging

class HandleRequests(object):
    '''
    classdocs：requests封装一层，对参数data、json进行区分
    '''

    def __init__(self):
        '''
        Constructor：初始化requests对象
        '''
        self.http = requests.Session()

    def __call__(self, method, url, data=None, **kwargs):
        """魔术方法调用"""

        self.method = method.upper()
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except json.JSONDecodeError as error:
                data = eval(data)
                logging.error("{}数据中包含了python对象,如:None\False\True,不能再转成dict对象:{}".format(data, error))
        if self.method == "POST":
            res = self.http.request(self.method, url, json=data, verify=True, **kwargs)
        elif self.method == "GET":
            res = self.http.request(self.method, url, params=data, verify=True, **kwargs)
        else:
            logging.info("请求方法{},暂不支持!!!".format(self.method))
        return res
