import jaydebeapi
import readConfig as readConfig

localReadConfig = readConfig.ReadConfig()

class MyPhoenix:
    def __init__(self):
        global database_url
        database_url = localReadConfig.get_phoenix("url")

    def PhoenixDEL(self, tableName=""):
        '''phoenix删除数据'''
        conn = jaydebeapi.connect('org.apache.phoenix.jdbc.PhoenixDriver', \
                                  'jdbc:phoenix:guoding002:2181',
                                  {'phoenix.schema.isNamespaceMappingEnabled': 'true'},
                                  'E:/workSpace/Config/phoenix-5.0.0-HBase-2.0-client.jar')
        curs = conn.cursor()
        tables = ['EVENT_ATTR_RECORD', 'EVENT_RECORD', 'SMS_RECORD', 'USER_BAG_RECORD', 'USER_TAG_RECORD',
                  'USER_HISTORY']
        for table in tables:
            sql = 'drop table '+tableName+'.' + table
            print(sql)
            curs.execute(sql)
            conn.commit()
        curs.close()
        conn.close()


if __name__ == '__main__':
    MyPhoenix().executeSQL()