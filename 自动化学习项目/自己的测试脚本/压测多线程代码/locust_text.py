# 压力测试
from locust import HttpUser, TaskSet, task, constant
from locust import User, task, between
import json


class Testlocust(TaskSet):
    # 循环100次
    @task(1000)
    def common_appconfig(self):
        post_url = 'http://192.168.0.64:7472/patient/create'
        header = {
            'Content-Type': 'application/json;charset=UTF-8',
        }
        dic_= {"icCard":"000001","patName":"测试1","birth":"111","sex":1,"phone":"1345141123121"}
        json_ = json.dumps(dic_)
        print(post_url)
        r = self.client.post(post_url, headers=header, json=json_)
        print("common_appconfig:", r)
        # assert r.idx == "0a871e93-5e47-4d0b-8c9a-27eece46d71f"
    #
    # @task(1000)
    # def user_order_list(self):
    #     post_url = "/test/user_order_list?max=0&include_paying=1&ct=dingzhi&ver=2&app=4&ut=.moWY1CvEFndLeTHLXD8&pf=android"
    #     header = {
    #         'Accept-Encoding': 'gzip, deflate',
    #         'Content-Type': 'application/json;charset=UTF-8',
    #         "Cookie": ""
    #     }
    #     r = self.client.get(post_url, headers=header)
    #     # print("user_order_list:", r)

class WebsiteUser(HttpUser):
    tasks = [Testlocust]
    min_wait = 500
    max_wait = 5000


##下面这些可以不用写
if __name__ == '__main__':
    import os
    # 如果利用多核心跑并发数
    # 一个终端启动主节点 "locust -f game_test2.py --master"
    # 多个终端启动多个work就会跑多个核心 locust -f game_test2.py --worker

    os.system('locust -f locust_text.py --web-host="127.0.0.1"')