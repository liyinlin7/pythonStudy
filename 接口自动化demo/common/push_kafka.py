"""
kafka推送模块
"""
import json


from confluent_kafka import Producer
KAFKA_ADDRS = "卡夫卡地址"


class ToKafka(object):

    def __init__(self):
        self.p = self.conn_ka()

    # kafka回调
    @staticmethod
    def delivery_report(err, msg):
        if err is not None:
            print(f"kafka数据传送失败： {err}")

    # 读取连接Kafka
    @staticmethod
    def conn_ka():
        kafka_addrs = KAFKA_ADDRS
        if kafka_addrs:
            producer = Producer({'bootstrap.servers': kafka_addrs})
        else:
            producer = ''
        return producer

    # 统一推送数据
    def push_data(self, topic, data_dict, key =None):
        tracer_data = json.dumps(data_dict, ensure_ascii=False)
        if key:
            print(f"{topic}当前推送的key为{key}")
            # 第三个参数key值
            self.p.produce(topic, tracer_data, key,
                           callback=self.delivery_report)
        else:
            self.p.produce(topic, tracer_data,
                           callback=self.delivery_report)
        self.p.flush()

    def push_to_kafka(self, data_dict, topic):
        if self.p == '':
            print(f"本地数据{data_dict}")
        else:
            self.p.poll(0)
            key = data_dict.get("id")
            self.push_data(key, topic, data_dict)


if __name__ == '__main__':
    a = {"id": "37338041", "game_id": 1, "source": 1, "create_time": 1611933142, "league_id": "37324360", "status": 3, "start_time": 1611922920, "end_time": 1611944520, "bo": 3, "win_team": "5414708", "has_odds": 2, "has_inplay": 1, "teams": [{"team": {"id": "5414708", "source": 1, "create_time": 1611933142, "game_id": 1, "name_full": "CES", "name_abbr": "", "country": "", "area": "", "pic": "https://www.nmgdjkj.com/file/ffe7e1d0a4d029b76bd749730f51cf88.png"}, "score": 2, "index": 1}, {"team": {"id": "35668833", "source": 1, "create_time": 1611933142, "game_id": 1, "name_full": "Secret", "name_abbr": "", "country": "", "area": "", "pic": "https://www.nmgdjkj.com/file/a58ff4551c546d2e0bdcd08ac4a86bea.png"}, "score": 1, "index": 2}]}
    ToKafka().push_to_kafka(a, 'original-series')
