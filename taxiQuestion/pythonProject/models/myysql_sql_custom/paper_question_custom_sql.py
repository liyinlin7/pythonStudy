from sqlalchemy import text
from models.mySql_mode import MySqlMode

class PaperQuestionCustomSql(MySqlMode):

    def paper_question_install_custom(self,paper_id, question_id, question_answer, user_answer=None, question_bool=None):
        sql = f"""INSERT INTO `taxi`.`paper_questions` (`paper_id`,`question_id`,`question_answer`,`user_answer`,`question_bool`) 
        VALUES (:paper_id, :question_id, :question_answer, :user_answer, :question_bool);"""
        with self.session.begin():
            result = self.session.execute(text(sql), {
                "paper_id": paper_id,
                "question_id": question_id,
                "question_answer": question_answer,
                "user_answer": user_answer,
                "question_bool": question_bool
            })
            rows_affected = result.rowcount
            if rows_affected == 0:
                return f"题目试卷关联插入{question_id}失败"
            else:
                return f"{question_id}插入成功"
    def paper_question_select(self,paperId, questionBool, questionId):
        sql = f"""SELECT * FROM  `taxi`.`paper_questions` WHERE `paper_id` = :paperId"""
        if questionBool and questionBool != 'undefined':
            sql += f" AND `question_bool` = :questionBool"
        if questionId and questionId != 'undefined':
            sql += f" AND `question_id` = :questionId"
        sql += f" limit 0, 10000;"
        with self.session.begin():
            result = self.session.execute( text( sql ), {
                "paperId": paperId,
                "questionBool": questionBool,
                "questionId": questionId
            } )
            total_count = result.rowcount
            rows = result.fetchall()
        __result = []
        for row in rows:
            row_map = {
                "paper_id": row[0],
                "question_id": row[1],
                "question_answer": row[2],
                "user_answer": row[3],
                "question_bool": row[4]
            }
            __result.append(row_map)
        return __result, total_count
    def paper_question_update(self,paperId, questionId, userAnswer, questionBool):
        sql = f"""update taxi.paper_questions set user_answer= :userAnswer, question_bool= :questionBool
        where paper_id = :paperId and question_id= :questionId ;"""
        with self.session.begin():
            result = self.session.execute( text( sql ), {
                "paperId": paperId,
                "userAnswer": userAnswer,
                "questionId": questionId,
                "questionBool": questionBool
            } )
        rows_affected = result.rowcount
        if rows_affected == 0:
            return f"提交答案失败"
        else:
            return f"提交成功"
    def paper_question_err(self,questionBool):
        sql = f"""SELECT question_id FROM  `taxi`.`paper_questions` WHERE `question_bool` = :questionBool  group by question_id"""
        with self.session.begin():
            result = self.session.execute( text( sql ), {
                "questionBool": questionBool
            } )
        # total_count = result.rowcount
        __result = result.fetchall()
        result = ''
        for row in __result:
            result += row[0] + ','
        return result

if __name__ == '__main__':
    from models.my_sql_driver import MySqlDriver
    my_sql_driver = MySqlDriver()
    # engine, session = my_sql_driver.connect_mysql()
    # engine, session = my_sql_driver.mysql_repeat(engine, session)
    question_sql = PaperQuestionCustomSql()
