import datetime
import json
import requests
import logging
import threading
import time
import sys
from time import sleep, ctime

# 参考地址 # https://blog.csdn.net/weixin_50271247/article/details/109242117
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
reponse_time = []
OK = []
errorCount = []

class runScript():

    def API(self, url, params):
        try:
            r = requests.get(url, params=params, timeout=10)
            #print(r.status_code)
            code = r.status_code
            if code != 200:
                print(code)
                errorCount.append[1]
            else:
                js = json.dumps(r.json())
                #print(r.json()) #json格式的响应数据
                # print(r.elapsed.total_seconds())　响应时间
                #print("ooo" + js) #没有解码的响应数据
                return [r.json(), r.elapsed.total_seconds(), js]
            #r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
        except requests.RequestException as e:
            print('failed.' + e)
            errorCount.append[1]

    def circulation(self, url, params):
        status = 0
        datas = "none."
        try:
            obj = self.API(url, params)
            if obj != None:
                #print(obj)
                reponse_time.append(obj[1])
                datas = json.loads(obj[2])["Msg"]
                status = json.loads(obj[2])["Code"]
                OK.append(datas)
        except Exception as e:
            return

def test(url, params):
    Restime = runScript()
    Restime.circulation(url, params)
def main(num, url, params):
    print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
    start_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %f')
    threads = []
    for i in range(num):
        t = threading.Thread(target=test, args=(url, params))
        threads.append(t)
    for t in range(num):
        threads[t].start()
        #time.sleep(0.0001)
    for j in range(num):
        threads[j].join()
    print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
    print("Starting at:", start_time)
    print("All done at:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S %f'))
    # print(OK)
    print('线程数：', len(threads))
    print('响应次数：', len(reponse_time))
    print('正常响应次数：', len(OK))
    print('错误次数：', len(errorCount))
    print('总响应最大时长：', (0 if len(reponse_time)==0 else max(reponse_time)))
    print('总响应最小时长：', (0 if len(reponse_time)==0 else min(reponse_time)))
    print('总响应时长：', (0 if len(reponse_time)==0 else sum(reponse_time)))
    print('平均响应时长：', (0 if len(reponse_time)==0 else (sum(reponse_time) / len(reponse_time))))
    # print('QPS（TPS）= 并发数/平均响应时间:',num  / (sum(reponse_time) / len(reponse_time)))

if __name__ == '__main__':
    num = input('输入需要开启的线程数量:')
    url = 'http://192.168.11.35:8598/test.html'  # 地址
    params = {'UserName': 'admin', 'UserPwd': '123456'}  # 参数
    main(int(num), url, params)
