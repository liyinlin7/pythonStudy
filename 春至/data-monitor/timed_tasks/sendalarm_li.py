import requests
from common import read_path
from common.read_config import ReadConfig
import json


class SendAlarm:

    # def send_dingtalk_alarm(self, msg):
    #     """向钉钉发送警报"""
    #     url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'dingtalk_alarm_url')
    #     data = '{"msgtype": "text","text": {"content": "测试结果：' + msg + '"}}'
    #     header = {'Content-Type': 'application/json'}
    #     requests.post(url, json=eval(data), headers=header)

    def send_alarm_python(self, title, people, msg, env_flag):
        """向钉钉发送警报"""
        if env_flag == 'release':
            url = ReadConfig().read_config(read_path.conf_path, 'BASE_DING', 'dingtalk_alarm_url')
            # url = "https://oapi.dingtalk.com/robot/send?access_token=61e11d9fbe2e96aa57f9c0b11fa83ea076517fb891e0ac17233cef076bceceaf"
        elif env_flag == 'develop':
            url = ReadConfig().read_config(read_path.conf_path, 'TEST_DING', 'dingtalk_alarm_url')
            # url = "https://oapi.dingtalk.com/robot/send?access_token=36366f08315f82183dff2878cc1c3a4b2734647c96dc4d5707043313cc8ba04d"
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
        # print(data)
        requests.post(url=url, json=data, headers=header)

    def send_alarm_python_(self, title, people, msg, env_flag):
        """SQL向钉钉发送警报(审核群)"""
        if env_flag == 'release':
            url = ReadConfig().read_config(read_path.conf_path, 'BASE_DING', 'sql_ding_url')
            # url = "https://oapi.dingtalk.com/robot/send?access_token=15f86d2d73db716e4ebac4b5095960e192d0dd0394f3598abcf713809381d651"
        elif env_flag == 'develop':
            url = ReadConfig().read_config(read_path.conf_path, 'TEST_DING', 'sql_ding_url')
            # url = "https://oapi.dingtalk.com/robot/send?access_token=c7e196473d3a34eb7d98613b16611f638e8a488854c5c64de3cf70be6fb10470"

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
        # print(data)
        requests.post(url=url, json=data, headers=header)


    def send_playway_dingtalk(self, title, people, msg, env_flag):
        '''
            指数钉钉预警
            钉钉机器人 关键词“指数预警”
            https://oapi.dingtalk.com/robot/send?access_token=f40270fedbad514c3986ae9d670ed8179b984e27335ad289e94eb4ce5cda2c0d
        :param msg:
        :return:
        '''
        if env_flag == 'release':
            url = ReadConfig().read_config(read_path.conf_path, 'BASE_DING', 'dingtalk_playway_url')
            # url = "https://oapi.dingtalk.com/robot/send?access_token=f40270fedbad514c3986ae9d670ed8179b984e27335ad289e94eb4ce5cda2c0d"
        elif env_flag == 'develop':
            url = ReadConfig().read_config(read_path.conf_path, 'TEST_DING', 'dingtalk_playway_url')
            # url = "https://oapi.dingtalk.com/robot/send?access_token=cfa6bd2200f30ad4601b077f92a1c1f276f7ad3cf7a2315e51b0ed7409fb2f9f"
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
        # print(data)
        requests.post(url=url, json=data, headers=header)

    def send_weishenda_examine(self, title, people, msg, env_flag):
        '''
            卫视达预警钉钉
            钉钉机器人 关键词“预警”
            https://oapi.dingtalk.com/robot/send?access_token=f40270fedbad514c3986ae9d670ed8179b984e27335ad289e94eb4ce5cda2c0d
        :param msg:
        :return:
        '''
        if env_flag == 'release':
            url = ReadConfig().read_config(read_path.conf_path, 'BASE_DING', 'weishida_url')
            # url = "https://oapi.dingtalk.com/robot/send?access_token=ec8624eb7e68790b446f740c3da92df29924dc977096d96239caa4f4c1f64d13"
        # elif env_flag == 'develop':
        #     url = ReadConfig().read_config(read_path.conf_path, 'TEST_DING', 'weishida_url')
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
        # print(data)
        requests.post(url=url, json=data, headers=header)


# if __name__ == '__main__':
#     # SendAlarm().send_alarm_text('测试报警！！！')
#     SendAlarm().send_dingtalk_alarm('测试报警！！！')
