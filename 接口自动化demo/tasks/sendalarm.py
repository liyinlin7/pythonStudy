import requests
from common import read_path
from common.read_config import ReadConfig
import json


class SendAlarm:

    # def send_dingtalk_alarm(self, msg):
    #     """向钉钉发送警报"""
    #     url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'dingtalk_alarm_url')
    #     test_data = '{"msgtype": "text","text": {"content": "测试结果：' + msg + '"}}'
    #     header = {'Content-Type': 'application/json'}
    #     requests.post(url, json=eval(test_data), headers=header)

    def send_sport_test(self, env_flag, title, people, msg):
        """向钉钉发送警报--其他球类预警群SQL"""
        if env_flag == 0:
            url = ReadConfig().read_config(read_path.conf_path, 'TEST', 'dingding_sport')
            # url = ''
        elif env_flag == 1:
            url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'dingding_sport')
            # url = 'https://oapi.dingtalk.com/robot/send?access_token=3ffa6997786a4f86dac287d1c045111483157555758dedda84cc4884eeaf0c48'
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": f"{title}",
                "text": f"{people}预警:{title}\n" +
                        "> 测试结果：\n" +
                        f"> ##### {msg}",
                },
            "at": {
                "atMobiles": [
                    "15657880727",
                    "18978840274"
                ],
                "isAtAll": False
            }
        }
        header = {'Content-Type': 'application/json'}
        # print(url)
        requests.post(url=url, json=data, headers=header)

    def send_sports_playway(self, env_flag, title, people, msg):
        """向钉钉发送警报(指数--其他)"""
        if env_flag == 0:
            url = ReadConfig().read_config(read_path.conf_path, 'TEST', 'dingding_sport_ZS')
            # url = ''
        elif env_flag == 1:
            url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'dingding_sport_ZS')
            # url = 'https://oapi.dingtalk.com/robot/send?access_token=211088bd3ad1b450d9b2f1d43ea13431f2e012ade4458c4e5bba330f5d42e58c'
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": f"{title}",
                "text": f"{people}预警:{title}\n" +
                        "> 测试结果：\n" +
                        f"> ##### {msg}",
                },
            "at": {
                "atMobiles": [
                    "15657880727",
                    "18978840274"
                ],
                "isAtAll": False
            }
        }
        header = {'Content-Type': 'application/json'}
        # print(url)
        requests.post(url=url, json=data, headers=header)

    def send_weishenda_examine(self, title, people, msg, env_flag):
        '''
            卫视达预警钉钉
            钉钉机器人 关键词“指数预警”
            https://oapi.dingtalk.com/robot/send?access_token=f40270fedbad514c3986ae9d670ed8179b984e27335ad289e94eb4ce5cda2c0d
        :param msg:
        :return:
        '''
        if env_flag == 1:
            url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'weishida_url')
            # url = "https://oapi.dingtalk.com/robot/send?access_token=ec8624eb7e68790b446f740c3da92df29924dc977096d96239caa4f4c1f64d13"
        # elif env_flag == 'develop':
        #     url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'weishida_url')
        #     # url = ""
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": f"{title}",
                "text": f"{people}指数预警:{title}\n" +
                        "> 结果：\n" +
                        f"> ##### {msg}",
            },
            "at": {
                "atMobiles": [
                    "15657880727",
                    "18978840274"
                ],
                "isAtAll": False
            }
        }
        header = {'Content-Type': 'application/json'}
        # print(test_data)
        requests.post(url=url, json=data, headers=header)

# if __name__ == '__main__':
    # SendAlarm().send_alarm_text('测试报警！！！')
    # SendAlarm().send_sport_test('测试报警！！！')
