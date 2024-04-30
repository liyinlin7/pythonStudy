from models.my_sql_driver import MySqlDriver
from sqlalchemy import text


class QuestionInsert(object):
    """
        question表的插入语句
    """

    def __init__(self):
        self.mysql_driver = MySqlDriver()
        self.engine, self.session = self.mysql_driver.connect_mysql()

    def question_insert(self, value_data):
        """
        :param data:
        :return:
        """
        __sql = text("""
        insert into taxi.questions(question_id, question_answer, number, question_title, question_type, `range`, type)
        values (:question_id, :question_answer, :number, :question_title, :question_type, :range, :type);
        """)
        engine, session = self.mysql_driver.mysql_repeat(self.engine, self.session)
        try:
            session.execute(__sql, value_data)
        except:
            print('插入失败:', __sql)
        else:
            session.commit()

    def operation_insert(self, value_data):
        """
        :param data:
        :return:
        """
        __sql = text("""
        insert into taxi.questions(question_id, question_answer, number, question_title, question_type, correct_answer, `range`, type)
        values (:question_id, :question_answer, :number, :question_title, :question_type, :correct_answer ,:range, :type);
        """)
        engine, session = self.mysql_driver.mysql_repeat(self.engine, self.session)
        try:
            session.execute(__sql, value_data)
        except:
            print('插入失败:', __sql)
        else:
            session.commit()