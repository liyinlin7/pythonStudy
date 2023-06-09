import json
import time
import os
import etcd3
from confluent_kafka import Producer, Consumer, KafkaError

LEAGUE_TOPIC = 'original-league'
SERISE_TOPIC = "original-series"
TEAM_TOPIC = "original-team"
RATE_EX_GROUP_TOPIC = 'original-rate-ex-group'
LIVE_EVENT_TOPIC = 'original-live-event'  # 实时事件
LIVE_DATA_TOPIC = 'original-live-data'  # 实时数据


class To_kafka(object):
    def __init__(self, topic, series_id):
        self.topic = topic
        self.series_id = series_id
        self.p = self.conn_ka()

    # 读取连接Kafka
    def conn_ka(self):
        etcd_urls_key = os.environ.get('ETCD_URLS')
        print("基础获取的ETCD为", etcd_urls_key)
        # # 如果获取不到，就为空，不启动
        if etcd_urls_key == None:
            etcd_urls_key = ''
        etcd_urls = etcd_urls_key.split(",")
        print("基础切分的ETCD为", etcd_urls)
        e_k = etcd_urls[0].split(":")
        H = e_k[0]
        P = e_k[1]
        # 读取etcd里Kafka的地址
        print("切割的域名和端口为", H, P)
        etcd = etcd3.client(host=H, port=P)
        ETCD_RES = etcd.get('/develop/config/mq/kafka/common/host')
        BOOTSTRAP_SERVERS = ETCD_RES[0].decode().split(",")
        print("Kafka的集群地址为", BOOTSTRAP_SERVERS)
        bs = ",".join(BOOTSTRAP_SERVERS)  # xin
        print("bs", bs)
        # producer = Producer({'bootstrap.servers': bs})
        # return producer
        consumer = Consumer({
            'bootstrap.servers': bs,  # kafka所在ip地址，多个地址用逗号隔开。
            'group.id': 'data-test',
            'enable.auto.commit': False,  # 是否自动提交offset
            'default.topic.config': {
                'auto.offset.reset': 'latest'
            }
        })
        consumer.subscribe([self.topic])
        return consumer

    # def push_to_kafka(self, data, data_key, n):
    #     print("kafka的League数据", n, data)
    #     self.p.produce(LEAGUE_TOPIC, json.dumps(data).encode('utf-8'))

    def get_data(self, t):
        final_data = {}
        if self.topic == LIVE_DATA_TOPIC:
            msg_list = []
            # receive_time = int(time.time())
            while True:
                msg = self.p.poll(1.0)
                if msg is None:
                    continue
                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        continue
                    else:
                        print(msg.error())
                        break
                msg_value = msg.value().decode('utf-8')
                # 如果时间一致且series_id一致，则存储数据
                if eval(msg_value)['time_stamp'] == t and eval(msg_value)['series_id'] == self.series_id:
                    msg_list.append(msg_value)
                # 如果获取到的数据时间不一致，则退出循环
                if eval(msg_value)['time_stamp'] != t:
                    break

            if len(msg_list) > 0:
                final_data = msg_list[-1]
            else:
                final_data = msg_list
        self.p.close()
        return final_data


if __name__ == '__main__':
    while True:
        t = int(time.time())
        print('当前时间：', t)
        s = To_kafka(LIVE_DATA_TOPIC, '2343103').get_data(t)
        print('Time:{}  Message:{}'.format(t, s))
        time.sleep(1)
