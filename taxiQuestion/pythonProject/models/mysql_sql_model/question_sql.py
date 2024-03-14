from sqlalchemy import create_engine, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, joinedload, aliased
from models.sql_table_model.user_answer import UserAnswer
from models.sql_table_model.questions import Questions
from sqlalchemy import and_

class QuestionSql(object):

    def __init__(self, engine, session):
        self.engine = engine
        self.session = session

    def question_select(self, question_id = '2', question_type = None):
        if question_id is None and question_type is None:
            questions = self.session.query(Questions).all()
        elif question_id and question_type is None:
            questions = self.session.query(Questions).filter( Questions.question_id == question_id )
        elif question_id and question_type:
            questions = self.session.query(Questions).filter( and_(Questions.question_type == question_type, Questions.question_id == question_id ))
        questions_as_dict = [
            {
                'question_id': question.question_id,
                'question_answer': question.question_answer,
                'question_option': question.question_option,
                'question_title': question.question_title,
                'question_type': question.question_type,
                'range': question.range,
                'type': question.type,
            } for question in questions
        ]
        print( questions_as_dict )
        return questions_as_dict

    def question_leftjoin_userAnswer(self):
        query = self.session.query( UserAnswer, Questions ).outerjoin( UserAnswer, and_(Questions.question_id == UserAnswer.question_id ))
        questions = query.all()
        questions_as_dict = [
            {
                'question_id': question.question_id,
                'question_answer': question.question_answer,
                'question_option': question.question_option,
                'question_title': question.question_title,
                'question_type': question.question_type,
                'range': question.range,
                'type': question.type,
                'user_question_id': UserAnswer.question_id,
                'user_answer': UserAnswer.user_answer,
                'answer_bool': UserAnswer.answer_bool,
            } for question in questions
        ]
        print( questions_as_dict )
        return questions_as_dict

if __name__ == '__main__':
    from models.my_sql_driver import MySqlDriver
    my_sql_driver = MySqlDriver()
    engine, session = my_sql_driver.connect_mysql(env_flag=0)
    question_sql = QuestionSql(engine, session)
    # question_sql.question_select()
    question_sql.question_leftjoin_userAnswer()
