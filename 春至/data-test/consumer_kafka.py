import json
import time
import logging
import os
import etcd3
from confluent_kafka import Consumer, KafkaError
from threading import Thread
from common.do_mysql import DoMySql
from common import my_logger, read_path
from common.read_config import ReadConfig

CSGO_LIVE_DATA = 'original-live-data-csgo'  # csgo实时数据
CSGO_LIVE_EVENT = 'original-live-event-csgo'    # csgo实时事件
CSGO_LIVE_EVENT_SPECIAL = 'original-live-special-event-csgo'  # csgo实时特殊事件
LOL_LIVE_DATA = 'original-live-data-lol'  # lol实时数据
LOL_LIVE_EVENT = 'original-live-event-lol'  # lol实时事件和特殊事件
LOL_RESULT_DATA = 'original-result-data-lol'  # lol赛果数据
KOG_RESULT_DATA = 'original-result-data-kog'  # 王者赛果数据
KOG_EVENT = 'original-live-event-kog'  # 王者实时事件

topic = eval(ReadConfig().read_config(read_path.conf_path, 'TOPIC', 'topic_dic'))
# series_list = ['574929', '571886', 'dotaS00008381']
series_list = ['575632']
# series_list = ['dotaS00008332']
id = ['15978']


class To_kafka(object):
    def __init__(self, topic):
        self.topic = topic
        self.c_data = self.conn_ka(topic)

    # 读取连接Kafka
    def conn_ka(self, topic):
        cur_time = int(round(time.time()*1000))
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
            'group.id': 'data-test1',
            'enable.auto.commit': False,  # 是否自动提交offset
            'default.topic.config': {
                # 'auto.offset.reset': 'latest',  # 实时事件
                'auto.offset.reset': 'earliest',  # 历史事件
            }
        })
        consumer.subscribe([topic])
        # tps = [TopicPartition(topic, tp, 1597110600000) for tp in range(5)]
        # offsets = consumer.offsets_for_times(tps)
        # consumer.assign(offsets)
        return consumer

    def get_data(self):

        cnn = DoMySql().connect(env_flag=0)
        while True:
            # 实时数据
            msg = self.c_data.poll(1.0)
            # print(msg.topic())
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break
            msg_value = msg.value().decode('utf-8')
            try:
                msg_dic = json.loads(msg_value)
            except Exception:
                print('11111111:::::', msg_value)
            if msg_dic['series_id'] in series_list:
                print(msg_value)
                logging.info(msg_value)
                DoMySql().insert_data(cnn, msg_value, self.topic)
            # if msg_dic['id'] in id:
            #     print(msg_value)
            #     logging.info(msg_value)
            #     DoMySql().insert_data(cnn, msg_value, self.topic)

        self.c_data.close()
        cnn.close()


if __name__ == '__main__':
    # data = [CSGO_LIVE_DATA, CSGO_LIVE_EVENT, CSGO_LIVE_EVENT_SPECIAL]
    #         实时数据         实时事件         实时特殊事件
    # data = [KOG_RESULT_DATA]
    # data = [topic['LOL_LIVE_DATA'], topic['LOL_LIVE_EVENT'], topic['LOL_LIVE_EVENT_SPECIAL']]
    # data = [topic['KOG_RESULT_DATA'], topic['KOG_EVENT']]
    # data = [topic['KOG_RESULT_DATA'], topic['KOG_EVENT']]
    # data = [topic['PLAYER_DATA']]
    # data = [topic['CSGO_RESULT_DATA']]
    # data = [topic['LOL_RESULT_DATA'], topic['DOTA_MATCH_DATA']]
    # data = [topic['DOTA_MATCH_DATA']]
    # data = [topic['DOTA_RESULT_DATA']]
    data = [topic['LOL_RESULT_DATA']]
    t_list = []
    for i in data:
        t = Thread(target=To_kafka(i).get_data)
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()

    # t1 = Thread(target=To_kafka(LIVE_DATA_TOPIC, 'csgo_live_data').get_data)
    # t2 = Thread(target=To_kafka(LIVE_EVENT_TOPIC, 'csgo_live_event').get_data)
    # t3 = Thread(target=To_kafka(LIVE_EVENT_SPECIAL_TOPIC, 'csgo_live_special_event').get_data)
    #
    # # 启动线程  ：异步执行的状态
    # t1.start()
    # t2.start()
    # t3.start()
    # t1.join()  # 默认等待子线程1执行结束
    # t2.join()  # 默认等待子线程2执行结束
    # t3.join()
