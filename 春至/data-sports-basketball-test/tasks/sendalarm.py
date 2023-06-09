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

    def send_sport_test(self, env_flag, title, people, msg):
        """向钉钉发送警报--篮球预警群"""
        if env_flag == 0:
            url = ReadConfig().read_config(read_path.conf_path, 'TEST', 'dingding_sport')
            # url = 'https://oapi.dingtalk.com/robot/send?access_token=f4238b2a1d7e2b4c9de365e8a85f6fd93af059b75daae32eef1d9dae49718a5c'
        elif env_flag == 1:
            url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'dingding_sport')
            # url = 'https://oapi.dingtalk.com/robot/send?access_token=150482cc472c1f214fec67a0144997c26207c16e44a706c4d875f0a8fcd4aa3b'
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

    def send_sport_test_SH(self, env_flag, title, people, msg):
        """向钉钉发送警报(审核_体育)"""
        if env_flag == 0:
            url = ReadConfig().read_config(read_path.conf_path, 'TEST', 'dingding_sport_SH')
            # url = 'https://oapi.dingtalk.com/robot/send?access_token=477345220e5f741a70d5e49597555e1ee4b89a0fb65703e5cc33608a76c3cced'
        elif env_flag == 1:
            url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'dingding_sport_SH')
            # url = 'https://oapi.dingtalk.com/robot/send?access_token=81ce3addcdca59cb94afc6cf30b1be6e6b8e329a167895707ea4c72934f47d82'
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

    # def send_alarm_python_(self, env_flag, title, people, msg):
    #     """向钉钉发送警报"""
    #     if env_flag == 0:
    #         url = ReadConfig().read_config(read_path.conf_path, 'TEST', 'dingding_sport')
    #         # url = 'https://oapi.dingtalk.com/robot/send?access_token=9cfbd3ac10135c2192a02b3865c1f9d8d29a7dbecb29ab2ad826bb4912dc76fb'
    #     elif env_flag == 1:
    #         url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'dingding_sport')
    #         # url = 'https://oapi.dingtalk.com/robot/send?access_token=2f9b312ba6d969f0278aa6bbed74c979b74473904dbdcd5044a610915034423f'
    #     data = {
    #         "msgtype": "markdown",
    #         "markdown": {
    #             "title": f"{title}",
    #             "text": f"{people}预警:{title}\n" +
    #                     "> 测试结果：\n" +
    #                     f"> ##### {msg}",
    #         },
    #         "at": {
    #             "atMobiles": [
    #                 "15657880727",
    #                 "18978840274"
    #             ],
    #             "isAtAll": False
    #         }
    #     }
    #
    #     header = {'Content-Type': 'application/json'}
    #     # print(data)
    #     requests.post(url=url, json=data, headers=header)

    def send_alarm_python_dianjing(self, title, people, msg, env_flag):
        """SQL向钉钉发送警报（审核电竞群）"""
        if env_flag == 1:
            url = "https://oapi.dingtalk.com/robot/send?access_token=15f86d2d73db716e4ebac4b5095960e192d0dd0394f3598abcf713809381d651"
        elif env_flag == 0:
            url = "https://oapi.dingtalk.com/robot/send?access_token=c7e196473d3a34eb7d98613b16611f638e8a488854c5c64de3cf70be6fb10470"
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

    def send_sports_playway(self, env_flag, title, people, msg):
        """向钉钉发送警报"""
        if env_flag == 0:
            url = ReadConfig().read_config(read_path.conf_path, 'TEST', 'dingding_sport_play')
            # url = 'https://oapi.dingtalk.com/robot/send?access_token=20ecec0052a3d5abbd20a9cc71102b4652c708cc5f4242d92790ce1b84912c00'
        elif env_flag == 1:
            url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'dingding_sport_play')
            # url = 'https://oapi.dingtalk.com/robot/send?access_token=5ab7652bbe1efcf88f2f95e173e9a8621bb5d993ff79331a90280b2808fbdc25'
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": f"{title}",
                "text": f"{people}指数预警:{title}\n" +
                        "> 测试结果：\n" +
                        f"> ##### {msg}",
            },
            "at": {
                "atMobiles": [
                    "15657880727",
                    "17623899724"
                ],
                "isAtAll": False
            }
        }
        header = {'Content-Type': 'application/json'}
        requests.post(url=url, json=data, headers=header)

# if __name__ == '__main__':
    # SendAlarm().send_alarm_text('测试报警！！！')
    # SendAlarm().send_sport_test('测试报警！！！')
