import datetime
import requests
from common import read_path
from common.read_config import ReadConfig
import json


class SendAlarm:

    def send_dingtalk_alarm(self, msg):
        """向钉钉发送警报"""
        url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'dingtalk_alarm_url')
        data = '{"msgtype": "text","text": {"content": "测试结果：' + msg + '"}}'
        header = {'Content-Type': 'application/json'}
        requests.post(url, json=eval(data), headers=header)

    def send_dingtalk_sql_r(mylist):
        """向钉钉发送警报"""
        header = {'Content-Type': 'application/json ;charset=utf-8'}
        # messageUrl = "https://oapi.dingtalk.com/robot/send?" \
        #              "access_token=61e11d9fbe2e96aa57f9c0b11fa83ea076517fb891e0ac17233cef076bceceaf"
        messageUrl = 'https://oapi.dingtalk.com/robot/send?access_token=3d02e50c4dc527d4e5f1d9618d477cb9457b8f4b229fbe81fbca8341f32b6db1'
        message = {
            "msgtype": "markdown",
            "markdown": {
                "title": "sql预警报告",
                "text": "### sql预警测试报告:@15657880727\n" +
                        "> 测试结果：\n" +
                        "> ##### 本次总共执行" + str(mylist[0]) + '条sql语句，其中错误' + str(mylist[1]) + '条，错误sql为:\n' + mylist[2]},
            "at": {
                "atMobiles": [
                    "15657880727"
                ],
                "isAtAll": False
            }
        }
        message = json.dumps(message)
        requests.post(messageUrl, message, headers=header)

    def send_dingtalk_sql_b(mylist):
        """向钉钉发送警报"""
        header = {'Content-Type': 'application/json ;charset=utf-8'}
        messageUrl = "https://oapi.dingtalk.com/robot/send?" \
                     "access_token=61e11d9fbe2e96aa57f9c0b11fa83ea076517fb891e0ac17233cef076bceceaf"
        # messageUrl = "https://oapi.dingtalk.com/robot/send?access_token=3d02e50c4dc527d4e5f1d9618d477cb9457b8f4b229fbe81fbca8341f32b6db1"
        message = {
            "msgtype": "markdown",
            "markdown": {
                "title": "sql预警报告",
                "text": "### sql预警测试报告:@18978840274\n" +
                        "> 测试结果：\n" +
                        "> ##### 本次总共执行" + str(mylist[0]) + '条sql语句，其中错误' + str(mylist[1]) + '条，错误sql为:\n' + mylist[2]},
            "at": {
                "atMobiles": [
                    "18978840274"
                ],
                "isAtAll": False
            }
        }
        message = json.dumps(message)
        requests.post(messageUrl, message, headers=header)

    def send_dingtalk_review(self, msg):
        """向钉钉发送警报"""
        url = 'https://oapi.dingtalk.com/robot/send?access_token=3d02e50c4dc527d4e5f1d9618d477cb9457b8f4b229fbe81fbca8341f32b6db1'
        # url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'dingtalk_alarm_url')
        if '系列赛' in msg:
            data = '{"msgtype": "text", "text": {"content": "测试结果：' + msg + '"}, "at": {"atMobiles": ["15657880727", "15988162049"], "isAtAll": false}}'
        else:
            data = '{"msgtype": "text","text": {"content": "测试结果：' + msg + '"}}'
        header = {'Content-Type': 'application/json'}
        data = json.loads(data)
        requests.post(url, json=data, headers=header)


    def send_dingtalk_match(self, msg):
        """向钉钉发送警报"""
        url = 'https://oapi.dingtalk.com/robot/send?access_token=3d02e50c4dc527d4e5f1d9618d477cb9457b8f4b229fbe81fbca8341f32b6db1'
        # url = ReadConfig().read_config(read_path.conf_path, 'BASE', 'dingtalk_alarm_url')
        if msg == '':
            print('1')
            data = '{"msgtype": "text","text": {"content": "测试结果:系列赛小局暂无问题！"}}'
        else:
            print('2')
            data = '{"msgtype": "text", "text": {"content": "测试结果：系列赛小局存在匹配不正常的数据' + msg + '"}, "at": {"atMobiles": ["18978840274"], "isAtAll": false}}'
        header = {'Content-Type': 'application/json'}
        data = json.loads(data)
        requests.post(url, json=data, headers=header)


if __name__ == '__main__':
    # SendAlarm().send_alarm_text('测试报警！！！')
    SendAlarm().send_dingtalk_alarm('测试报警！！！')
