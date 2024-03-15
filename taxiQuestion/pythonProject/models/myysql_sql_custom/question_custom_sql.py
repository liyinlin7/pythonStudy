from models.sql_table_model.questions import Questions
from models.sql_table_model.useranswer import UserAnswer
from sqlalchemy import and_
from models.mysql_resule import result_all_one, result_leftjoin_all_many
import logging
from common import my_logger

class QuestionCustomSql(object):

    def __init__(self, engine, session):
        self.engine = engine
        self.session = session

    def question_select_and(self, question_id:list=None, question_type:list=None):
        for var_name in ['question_id', 'question_type']:
            var_value = locals()[var_name]
            if var_value is not None:
                self.question_conditions[var_name] = var_value
        query = self.session.query( Questions )
        for field, value in self.question_conditions.items():
            if value is not None:  # 如果有值，添加为搜索条件
                query = query.filter( getattr( Questions, field ).in_(value) )
        result = query.all()
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
        #     } for question in result
        # ]
        # print( questions_as_dict )
        # return questions_as_dict

    def question_leftjoin_userAnswer_and(self, question_id:list=None, question_type:list=None, user_answer:list=None):
        for var_name in ['question_id', 'question_type']:
            var_value = locals()[var_name]
            if var_value is not None:
                self.question_conditions[var_name] = var_value
        for var_name in ['user_answer']:
            var_value = locals()[var_name]
            if var_value is not None:
                self.user_answer_conditions[var_name] = var_value
        query = (self.session.query( Questions, UserAnswer )
                 .outerjoin( UserAnswer, and_(Questions.question_id == UserAnswer.question_id )))
        # 添加 Questions 的搜索条件
        for field, value in self.question_conditions.items():
            if value is not None:  # 如果有值，添加为搜索条件
                query = query.filter( getattr( Questions, field ).in_(value) )
        # 添加 UserAnswer 的搜索条件
        for field, value in self.user_answer_conditions.items():
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


if __name__ == '__main__':
    from models.my_sql_driver import MySqlDriver
    my_sql_driver = MySqlDriver()
    engine, session = my_sql_driver.connect_mysql()
    engine, session = my_sql_driver.mysql_repeat(engine, session)
    question_sql = QuestionSql(engine, session)
    # question_sql.question_select_and()
    question_sql.question_leftjoin_userAnswer_and()
