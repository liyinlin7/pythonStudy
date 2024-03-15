from models.sql_table_model.questions import Questions
from models.sql_table_model.useranswer import UserAnswer
from sqlalchemy import and_
from models.mysql_resule import result_all_one, result_leftjoin_all_many
import logging
from common import my_logger
from sqlalchemy import text

class QuestionCustomSql(object):

    def __init__(self, engine, session):
        self.engine = engine
        self.session = session

    # def question_select_custom_and(self, question_id=['1','2'], question_type:list=['1','2']):
    def question_select_custom_and(self, question_id=None, question_type:list=None):
        conditions = []
        params = {}
        # 添加条件到查询中
        if question_id is not None:
            # sql += " where question_id = :question_id"
            # params['question_id'] = question_id
            placeholders_id = ', '.join( [':id' + str( i ) for i in range( len( question_id ) )] )
            conditions.append(" question_id IN (" + placeholders_id  + ")")
            # 为每个占位符添加对应的问题类型
            for i, id in enumerate( question_id ):
                params['id' + str( i )] = id
        if question_type is not None:
            # sql += " and question_type = :question_type"
            # params['question_type'] = question_type
            placeholders_type = ', '.join( [':type' + str( i ) for i in range( len( question_type ) )] )
            conditions.append(" question_type IN (" + placeholders_type + ")")
            # 为每个占位符添加对应的问题类型
            for i, type in enumerate( question_type ):
                params['type' + str( i )] = type
        # 构建SQL查询
        sql = "SELECT * FROM questions"
        if conditions:
            sql += " WHERE " + " AND ".join( conditions )
        # 执行查询
        with session.begin():
            result = session.execute( text( sql ), params )
            rows = result.fetchall()
            keys = result.keys()
        # 将结果转换为字典列表并打印
        result_dict = [dict(zip(keys, row)) for row in rows]
        print( result_dict )
        # questions_as_dict = [
        #     {
        #         'question_id': question.question_id,
        #         'question_answer': question.question_answer,
        #         'question_option': question.question_option,
        #         'question_title': question.question_title,
        #         'question_type': question.question_type,
        #         'range': question.range,
        #         'type': question.type,
        #     } for question in result
        # ]
        # print( questions_as_dict )
        # return questions_as_dict

    def question_leftjoin_userAnswer_coustom_and(self, question_id:list=None, question_type:list=None, user_answer:list=None):
    # def question_leftjoin_userAnswer_coustom_and(self, question_id=['1','2'], question_type:list=['2','3'],  user_answer:list=None):
        conditions = []
        params = {}
        # 添加条件到查询中
        if question_id is not None:
            # sql += " where question_id = :question_id"
            # params['question_id'] = question_id
            placeholders_id = ', '.join( [':id' + str( i ) for i in range( len( question_id ) )] )
            conditions.append( " questions.question_id IN (" + placeholders_id + ")" )
            # 为每个占位符添加对应的问题类型
            for i, id in enumerate( question_id ):
                params['id' + str( i )] = id
        if question_type is not None:
            # sql += " and question_type = :question_type"
            # params['question_type'] = question_type
            placeholders_type = ', '.join( [':type' + str( i ) for i in range( len( question_type ) )] )
            conditions.append( " questions.question_type IN (" + placeholders_type + ")" )
            # 为每个占位符添加对应的问题类型
            for i, type in enumerate( question_type ):
                params['type' + str( i )] = type
        if user_answer is not None:
            # sql += " where question_id = :question_id"
            # params['question_id'] = question_id
            placeholders_user_answer = ', '.join( [':username' + str( i ) for i in range( len( user_answer ) )] )
            conditions.append( " useranswer.user_answer IN (" + placeholders_user_answer + ")" )
            # 为每个占位符添加对应的问题类型
            for i, username in enumerate( user_answer ):
                params['username' + str( i )] = username
        sql = "SELECT * FROM questions left join useranswer on questions.question_id = useranswer.question_id"
        if conditions:
            sql += " WHERE " + " AND ".join( conditions )
        # 执行查询
        with session.begin():
            result = session.execute( text( sql ), params )
            rows = result.fetchall()
            keys = result.keys()
        result_dict = [dict( zip( keys, row ) ) for row in rows]
        print( result_dict )


if __name__ == '__main__':
    from models.my_sql_driver import MySqlDriver
    my_sql_driver = MySqlDriver()
    engine, session = my_sql_driver.connect_mysql()
    engine, session = my_sql_driver.mysql_repeat(engine, session)
    question_sql = QuestionCustomSql(engine, session)
    # question_sql.question_select_custom_and()
    question_sql.question_leftjoin_userAnswer_coustom_and()
