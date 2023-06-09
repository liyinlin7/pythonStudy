from test.National_dictionary import National_list
from common.do_mysql import DoMySql


class MysqlCountry(object):
    '''
        修改数据库  队伍和队员 country 字段
    '''

    def __init__(self):
        self.domysql = DoMySql()
        self.cnn_centon = self.domysql.cnn_centon
        self.cnn_basic = self.domysql.cnn_basic

    def player_country(self, even):
        '''
        队员
        :param even:
        :return:
        '''
        sql_country_group = '''
            SELECT *  FROM `data-basic`.player WHERE length( country ) = CHARACTER_LENGTH( country ) and country != ''  group by country order by country;
        '''
        if even == 0:  # 测试
            country_datas = self.domysql.select_centon(cnn=self.cnn_centon, sql=sql_country_group)
        elif even == 1:  # 线上
            country_datas = self.domysql.select_basic(cnn=self.cnn_basic, sql=sql_country_group)
        country_lists = []
        for i in country_datas:
            country_lists.append(i['country'])
        for i in country_lists:
            for y in National_list:
                county_en = y.get('name_abbr')
                county_zh = y.get('country')
                print("国家代码：", county_en)
                print("国家名称：", county_zh)
                if i == county_en:
                    update_sql = f'''
                        update `data-basic`.player set country = '{county_zh}' WHERE country = '{i}';
                    '''
                    print(update_sql)
                    if even == 0:
                        self.domysql.update_centon(cnn=self.cnn_centon, sql=update_sql)
                    elif even == 1:
                        self.domysql.update_basic(cnn=self.cnn_basic, sql=update_sql)

    def team_country(self, even):
        '''
        队员
        :param even:
        :return:
        '''
        sql_country_group = '''
            SELECT *  FROM `data-basic`.team WHERE length( country ) = CHARACTER_LENGTH( country ) and country != ''  group by country order by country;
        '''
        if even == 0:  # 测试
            country_datas = self.domysql.select_centon(cnn=self.cnn_centon, sql=sql_country_group)
        elif even == 1:  # 线上
            country_datas = self.domysql.select_basic(cnn=self.cnn_basic, sql=sql_country_group)
        country_lists = []
        for i in country_datas:
            country_lists.append(i['country'])
        for i in country_lists:
            team_country = str(i).upper()
            for y in National_list:
                county_en = y.get('name_abbr')
                county_zh = y.get('country')
                print("国家代码：", county_en)
                print("国家名称：", county_zh)
                if team_country == county_en:
                    update_sql = f'''
                        update `data-basic`.team set country = '{county_zh}' WHERE country = '{i}';
                    '''
                    print(update_sql)
                    if even == 0:
                        self.domysql.update_centon(cnn=self.cnn_centon, sql=update_sql)
                    elif even == 1:
                        self.domysql.update_basic(cnn=self.cnn_basic, sql=update_sql)


if __name__ == '__main__':
    my = MysqlCountry()
    my.player_country(1)
    my.team_country(1)


