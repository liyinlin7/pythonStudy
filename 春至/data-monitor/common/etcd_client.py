"""
从ETCD里读取配置信息
直接更新各配置
"""
import json
import os
from configparser import ConfigParser
from common import read_path

import etcd3

cfg_path = read_path.conf_path
print("配置文件地址：", cfg_path)


class WriteConf:

    def __init__(self):
        self.etcd = self.cli_etcd()
        self.cp = ConfigParser()
        self.cp.read(cfg_path, 'UTF-8')

    # 连接etcd
    def cli_etcd(self):
        etcd_urls_key = os.environ.get('ETCD_URLS')
        print(f"当前etcd地址为{etcd_urls_key}")
        if etcd_urls_key:
            etcd_urls = etcd_urls_key.split(",")
            etcd_url = etcd_urls[0].split(":")
            h, p = etcd_url[0], etcd_url[1]
            etcd = etcd3.client(host=h, port=p)
            return etcd
        # etcd = etcd3.client(host='47.114.175.98', port=2379)
        # etcd = etcd3.client(host='47.57.142.181', port=2379)
        # etcd = etcd3.client(host='47.57.231.50', port=21789)
        # return etcd

    # 读取环境变量
    def read_env(self):
        # env_key = self.etcd.get("/develop/config/python/environ")[0].decode()
        env_key = self.etcd.get("/local/config/python/environ")[0].decode()
        print("环境变量ENV：", env_key)
        return env_key

    # 读取mongo的配置
    def read_mysql(self):
        mysql_basic = self.etcd.get("/develop/config/mysql/data-basic")[0].decode()
        # mysql_basic = self.etcd.get("/develop/config/mysql/data-basic")[0].decode()
        mysql_centon = self.etcd.get("/develop/config/mysql/data-center")[0].decode()
        # mysql_centon = self.etcd.get("/develop/config/mysql/data-center")[0].decode()
        mysql_conf_centon = json.loads(mysql_centon)
        mysql_conf_basic = json.loads(mysql_basic)
        print("data-center:", mysql_conf_centon)
        print("data-basic:", mysql_conf_basic)
        mysql_host_centon = mysql_conf_centon.get("host")
        mysql_host_basic = mysql_conf_basic.get("host")
        mysql_port = mysql_conf_centon.get("port")
        mysql_pwd = mysql_conf_centon.get("password")
        mysql_user = mysql_conf_centon.get("user")
        return mysql_host_centon, mysql_host_basic, mysql_port, mysql_pwd, mysql_user

    def read_mongo(self):
        # mongo = self.etcd.get("/develop/config/mongo/python/data-result")[0].decode()
        mongo = self.etcd.get("/develop/config/mongo/python/data-result")[0].decode()
        mongo_conf = json.loads(mongo)
        print("mongoDB:", mongo_conf)
        mongo_host = mongo_conf.get("host")
        mongo_port = mongo_conf.get("port")
        mongo_pwd = mongo_conf.get("password")
        mongo_user = mongo_conf.get("user")
        mongo_database = mongo_conf.get("database")
        # mongo_authSource = mongo_conf.get("authSource")
        return mongo_host, mongo_port, mongo_pwd, mongo_user, mongo_database

    # # 读取Kafka集群地址
    # def read_kafka(self):
    #     kafka = self.etcd.get('/develop/config/mq/kafka/common/host')
    #     bootstart_servers = kafka[0].decode().split(",")
    #     print(f"kafka地址{kafka},Kafka的集群地址{bootstart_servers}")
    #     bs = ",".join(bootstart_servers)
    #     return bs  # kafka的集群地址
    #
    # # 读取redis配置
    # def read_redis(self):
    #     redis_ = self.etcd.get("/develop/config/cache/python/redis")[0].decode()
    #     redis_conf = json.loads(redis_)
    #     redis_host = redis_conf.get("host")
    #     redis_pwd = redis_conf.get("password")
    #     redis_port = redis_conf.get("port")
    #     redis_db = '1'
    #     return redis_host, redis_port, redis_pwd, redis_db

    # 写入配置文件
    def write_cfg(self):
        env_key = self.read_env()
        mysql_host_centon, mysql_host_basic, mysql_port, mysql_pwd, mysql_user = self.read_mysql()
        mongo_host, mongo_port, mongo_pwd, mongo_user, mongo_database = self.read_mongo()
        # print(env_key)
        # 环境写入
        self.cp.set('ENV', 'env', env_key)
        # mysql_centon 写入
        self.cp.set('MYSQL', 'host_centon', mysql_host_centon)
        self.cp.set('MYSQL', 'port', mysql_port)
        self.cp.set('MYSQL', 'user', mysql_user)
        self.cp.set('MYSQL', 'password', mysql_pwd)
        # mysql_basic 写入
        self.cp.set('MYSQL', 'host_basic', mysql_host_basic)
        # MongoDB写入
        self.cp.set('mongoDB', 'host', mongo_host)
        self.cp.set('mongoDB', 'port', mongo_port)
        self.cp.set('mongoDB', 'username', mongo_user)
        self.cp.set('mongoDB', 'password', mongo_pwd)
        self.cp.set('mongoDB', 'database', mongo_database)
        # self.cp.set('mongoDB', 'authSource', mongo_authSource)
        with open(cfg_path, 'w', encoding="utf-8") as f:
            self.cp.write(f)


if __name__ == '__main__':
    WriteConf().write_cfg()
