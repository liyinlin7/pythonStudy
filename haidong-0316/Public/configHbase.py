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
                                  'E:/workSpace/phoenix-5.0.0-HBase-2.0-client.jar')
        curs = conn.cursor()
        curs.execute('select * from test_table')
        curs.fetchall()


if __name__ == '__main__':
    MyPhoenix().executeSQL()