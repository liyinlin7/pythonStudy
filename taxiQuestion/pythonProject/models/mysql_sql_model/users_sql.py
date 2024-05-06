from models.sql_table_model.users import Users
from sqlalchemy import and_
from models.mysql_resule import result_all_one, result_leftjoin_all_many
from models.mySql_mode import MySqlMode
import logging
from common import my_logger

class UsersSql(MySqlMode):

    def __init__(self):
        super(UsersSql, self).__init__()
        self._engine, self._session = self.mysql_repeat(self.engine, self.session)

    def users_select_and(self, dic):
        """
           根据提供的问题ID和问题类型筛选问题。

           :param question_id: 一个包含问题ID的列表，可选参数，默认为None。
           :param question_type: 一个包含问题类型的列表，可选参数，默认为None。
           :return: 没有返回值，该函数目前打印查询结果，但注释表明之前有返回字典列表的意图。
           """
        password = dic.get( 'password' )
        user_phone = dic.get( 'user_phone' )
        columns = {
            'password': None,
            'user_phone': None,
        }
        for var_name in ['password', 'user_phone']:
            var_value = locals()[var_name]
            if var_value is not None:
                columns[var_name] = var_value
        query = self.session.query( Users )
        for field, value in columns.items():
            if value is not None:  # 如果有值，添加为搜索条件
                query = query.filter( getattr( Users, field ).in_(value) )
        result = query.all()
        if result is None:
            return None
        else:
            return True


if __name__ == '__main__':
    # from models.my_sql_driver import MySqlDriver
    # my_sql_driver = MySqlDriver()
    # engine, session = my_sql_driver.connect_mysql()
    # engine, session = my_sql_driver.mysql_repeat(engine, session)
    # users_sql = Users()

    import uuid
    print(uuid.uuid4())