from models.sql_table_model.questions import Questions
from models.sql_table_model.useranswer import UserAnswer
from sqlalchemy import and_
from models.mysql_resule import result_all_one, result_leftjoin_all_many
from models.mySql_mode import MySqlMode
import logging
from common import my_logger

class QuestionSql(MySqlMode):

    def __init__(self):
        super(QuestionSql, self).__init__()
        self._engine, self._session = self.mysql_repeat(self.engine, self.session)

    def question_select_and(self, dic, page_size, page_index):
        """
           根据提供的问题ID和问题类型筛选问题。

           :param question_id: 一个包含问题ID的列表，可选参数，默认为None。
           :param question_type: 一个包含问题类型的列表，可选参数，默认为None。
           :return: 没有返回值，该函数目前打印查询结果，但注释表明之前有返回字典列表的意图。
           """
        dic = dict(dic)
        print('dic', dic)
        type =  [dic.get( 'type_op' )] if dic.get( 'type_op' ) != '' and dic.get( 'type_op' ) is not None else None
        question_id = [dic.get( 'question_id' )] if dic.get( 'question_id') != '' and dic.get( 'question_id' ) is not None else None
        question_type = dic.get( 'question_type' ) if dic.get( 'question_type' ) != [] else None
        range = dic.get( 'range' ) if dic.get( 'range' ) != [] else None
        collect = dic.get( 'collect' ) if  dic.get( 'collect' ) != [] else None
        columns = {
            'question_id': None,
            'question_type': None,
            'type': None,
            'range': None,
            'collect': None
        }
        for var_name in ['question_id', 'question_type', 'type', 'range', 'collect']:
            var_value = locals()[var_name]
            if var_value is not None:
                columns[var_name] = var_value
        query = self.session.query( Questions )
        for field, value in columns.items():
            if value is not None:  # 如果有值，添加为搜索条件
                query = query.filter( getattr( Questions, field ).in_(value) )
        # 计算偏移量
        offset = (page_index - 1) * page_size
        # 执行查询并分页
        result = query.offset( offset ).limit( page_size ).all()
        total_count = query.count()
        __result = result_all_one(result)
        return __result, total_count

    def question_leftjoin_userAnswer_and(self, question_id:list=None, question_type:list=None, user_answer:list=None):
        question_conditions = {
            'question_id': None,
            'question_type': None,
        }
        user_answer_conditions = {
            'user_answer': None,
            'answer_bool': None
        }
        for var_name in ['question_id', 'question_type']:
            var_value = locals()[var_name]
            if var_value is not None:
                question_conditions[var_name] = var_value
        for var_name in ['user_answer']:
            var_value = locals()[var_name]
            if var_value is not None:
                user_answer_conditions[var_name] = var_value
        query = (self._session.query( Questions, UserAnswer )
                 .outerjoin( UserAnswer, and_(Questions.question_id == UserAnswer.question_id )))
        # 添加 Questions 的搜索条件
        for field, value in question_conditions.items():
            if value is not None:  # 如果有值，添加为搜索条件
                query = query.filter( getattr( Questions, field ).in_(value) )
        # 添加 UserAnswer 的搜索条件
        for field, value in user_answer_conditions.items():
            if value is not None:  # 如果有值，添加为搜索条件
                query = query.filter( getattr( UserAnswer, field ).in_(value) )
        result = query.all()
        fields_dict = {}
        table_name = []
        fields_dict['useranswer'] = UserAnswer.useranswer_key
        table_name.append(Questions.__tablename__)
        table_name.append(UserAnswer.__tablename__)
        __result = result_leftjoin_all_many( result, fields_dict, table_name )
        print( __result )
        return __result

    def question_types(self):
        query = self.session.query( Questions.type.distinct() )
        # query = self.session.query( Questions.type.distinct() ).group_by(Questions.type)
        results = query.all()
        __result = result_all_one(results)
        print( __result)
        return __result

if __name__ == '__main__':
    from models.my_sql_driver import MySqlDriver
    my_sql_driver = MySqlDriver()
    # engine, session = my_sql_driver.connect_mysql()
    # engine, session = my_sql_driver.mysql_repeat(engine, session)
    question_sql = QuestionSql()
    question_sql.question_select_and(dic={}, page_size=10, page_index=2)
    # question_sql.question_leftjoin_userAnswer_and(user_answer=['11', '33'])
