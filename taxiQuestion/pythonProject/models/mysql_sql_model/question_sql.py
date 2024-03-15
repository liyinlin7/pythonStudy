from models.sql_table_model.questions import Questions
from models.sql_table_model.useranswer import UserAnswer
from sqlalchemy import and_
from models.mysql_resule import result_all_one, result_leftjoin_all_many
import logging
from common import my_logger

class QuestionSql(object):

    def __init__(self, engine, session):
        self.engine = engine
        self.session = session


    def question_select(self, question_id = '2', question_type = '2'):
        search_conditions = {
            'question_id': question_id,
            'question_type': question_type
        }
        query = self.session.query( Questions )
        for field, value in search_conditions.items():
            if value is not None:  # 如果有值，添加为搜索条件
                query = query.filter( getattr( Questions, field ) == value )
        result = query.all()
        # if question_id is None and question_type is None:
        #     result = self.session.query(Questions).all()
        # elif question_type and question_id is None:
        #     result = self.session.query(Questions).filter( Questions.question_type == question_type )
        # elif question_id and question_type is None:
        #     result = self.session.query(Questions).filter( Questions.question_id == question_id )
        # elif question_id and question_type:
        #     result = self.session.query(Questions).filter( and_(Questions.question_type == question_type, Questions.question_id == question_id ))
        __result = result_all_one(result)
        print(__result)
        # questions_as_dict = [
        #     {
        #         'question_id': question.question_id,
        #         'question_answer': question.question_answer,
        #         'question_option': question.question_option,
        #         'question_title': question.question_title,
        #         'question_type': question.question_type,
        #         'range': question.range,
        #         'type': question.type,
        #     } for question in questions
        # ]
        # print( questions_as_dict )
        # return questions_as_dict

    def question_leftjoin_userAnswer(self):
        query = self.session.query( Questions, UserAnswer ).outerjoin( UserAnswer, and_(Questions.question_id == UserAnswer.question_id ))
        # query = self.session.query( Questions ).options( joinedload( Questions.useranswer ) ).all()
        result = query.all()
        fields_dict = {}
        table_name = []
        fields_dict['useranswer'] = UserAnswer.useranswer_key
        table_name.append(Questions.__tablename__)
        table_name.append(UserAnswer.__tablename__)
        __result = result_leftjoin_all_many( result, fields_dict, table_name )
        print( __result )


if __name__ == '__main__':
    from models.my_sql_driver import MySqlDriver
    my_sql_driver = MySqlDriver()
    engine, session = my_sql_driver.connect_mysql()
    engine, session = my_sql_driver.mysql_repeat(engine, session)
    question_sql = QuestionSql(engine, session)
    question_sql.question_select()
    # question_sql.question_leftjoin_userAnswer()