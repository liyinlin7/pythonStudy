from models.sql_table_model.paper import Paper
from models.sql_table_model.useranswer import UserAnswer
from sqlalchemy import and_
from models.mysql_resule import result_all_one, result_leftjoin_all_many
from models.mySql_mode import MySqlMode
from sqlalchemy import desc
import logging
from common import my_logger

class PaperSql(MySqlMode):

    def __init__(self):
        super(PaperSql, self).__init__()
        self._engine, self._session = self.mysql_repeat(self.engine, self.session)

    def paper_select_and(self, dic, page_size, page_index):
        """
           根据提供的问题ID和问题类型筛选问题。

           :param question_id: 一个包含问题ID的列表，可选参数，默认为None。
           :param question_type: 一个包含问题类型的列表，可选参数，默认为None。
           :return: 没有返回值，该函数目前打印查询结果，但注释表明之前有返回字典列表的意图。
           """
        dic = dict(dic)
        # print('dic', dic)
        paperId =  [dic.get( 'paperId' )] if dic.get( 'paperId' ) != '' and dic.get( 'paperId' ) is not None else None
        paperName = [dic.get( 'paperName' )] if dic.get( 'paperName') != '' and dic.get( 'paperName' ) is not None else None
        paperType = dic.get( 'paperType' ) if dic.get( 'paperType' ) != [] else None
        paperRange = dic.get( 'paperRange' ) if dic.get( 'paperRange' ) != [] else None
        paperQuestionType = dic.get( 'paperQuestionType' ) if  dic.get( 'paperQuestionType' ) != [] else None
        columns = {
            'paperId': None,
            'paperName': None,
            'paperType': None,
            'paperRange': None,
            'paperQuestionType': None
        }
        for var_name in ['paperId', 'paperName', 'paperType', 'paperRange', 'paperQuestionType']:
            var_value = locals()[var_name]
            if var_value is not None:
                columns[var_name] = var_value
        query = self.session.query( Paper )
        for field, value in columns.items():
            if value is not None:  # 如果有值，添加为搜索条件
                query = query.filter( getattr( Paper, field ).in_(value) )
        # 计算偏移量
        offset = (page_index - 1) * page_size
        # 执行查询并分页
        result = query.order_by(desc('createTime')).offset( offset ).limit( page_size ).all()
        total_count = query.count()
        __result = result_all_one(result)
        return __result, total_count


if __name__ == '__main__':
    from models.my_sql_driver import MySqlDriver
    my_sql_driver = MySqlDriver()
    # engine, session = my_sql_driver.connect_mysql()
    # engine, session = my_sql_driver.mysql_repeat(engine, session)
    question_sql = PaperSql()
    question_sql.paper_select_and(dic={}, page_size=10, page_index=2)
    # question_sql.question_leftjoin_userAnswer_and(user_answer=['11', '33'])
