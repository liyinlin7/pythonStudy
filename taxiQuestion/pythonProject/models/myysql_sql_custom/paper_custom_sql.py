from sqlalchemy import text
from models.mySql_mode import MySqlMode
from datetime import datetime
# 获取当前时间（但这里我们需要的是一个特定的示例时间，所以我们会手动创建一个）
# 获取当前时间



class PaperCustomSql(MySqlMode):

    # def question_select_custom_and(self, question_id=['1','2'], question_type:list=['1','2']):
    def paper_install_custom(self,paper_id, paper_name, paper_type, paper_range, paper_question_type):
        current_time = datetime.now()
        # 使用strftime方法来格式化时间
        formatted_time = current_time.strftime( '%Y-%m-%d %H:%M:%S' )
        print( formatted_time )  # 输出类似: 2023-07-19 14:23:23（具体取决于当前时间）
        sql = f"""INSERT INTO `taxi`.`paper` (`paperId`,`paperName`,`paperType`,`paperRange`,`paperQuestionType`,`createTime`) 
        VALUES (:paperId, :paperName, :paperType, :paperRange, :paperQuestionType, :createTime);"""
        with self.session.begin():
            result = self.session.execute(text(sql), {
                "paperId": paper_id,
                "paperName": paper_name,
                "paperType": str(paper_type) if paper_type != [] else None,
                "paperRange": str(paper_range) if paper_range != [] else None,
                "paperQuestionType": str(paper_question_type) if paper_question_type != [] else None,
                "createTime": formatted_time
            })
            rows_affected = result.rowcount
            if rows_affected == 0:
                return 0
            else:
                return f"{paper_id}试卷创建成功"

    def paper_select_custom_and(self,paper_id, paper_name, paper_type, paper_range, paper_question_type):
        current_time = datetime.now()
        # 使用strftime方法来格式化时间
        formatted_time = current_time.strftime( '%Y-%m-%d %H:%M:%S' )
        print( formatted_time )  # 输出类似: 2023-07-19 14:23:23（具体取决于当前时间）
        sql = f"""INSERT INTO `taxi`.`paper` (`paperId`,`paperName`,`paperType`,`paperRange`,`paperQuestionType`,`createTime`) 
        VALUES (:paperId, :paperName, :paperType, :paperRange, :paperQuestionType, :createTime);"""
        with self.session.begin():
            result = self.session.execute(text(sql), {
                "paperId": paper_id,
                "paperName": paper_name,
                "paperType": paper_type,
                "paperRange": paper_range,
                "paperQuestionType": paper_question_type,
                "createTime": formatted_time
            })
            rows_affected = result.rowcount
            if rows_affected == 0:
                return "没有插入任何记录"
            else:
                return f"插入了{rows_affected}条记录"

    def paper_delete(self, paperId):
        sql = f"""DELETE FROM `taxi`.`paper` WHERE `paperId` = :paperId;"""
        with self.session.begin():
            result = self.session.execute(text(sql), {
                "paperId": paperId
            })
            rows_affected = result.rowcount
            if rows_affected == 0:
                return 0
            else:
                return f"删除了{rows_affected}条记录"

    def paper_question_delete(self, paperId):
        sql = f"""DELETE FROM `taxi`.`paper_questions` WHERE `paper_id` = :paperId;"""
        with self.session.begin():
            result = self.session.execute(text(sql), {
                "paperId": paperId
            })
            rows_affected = result.rowcount
            if rows_affected == 0:
                return 0
            else:
                return f"删除了{rows_affected}条记录"



if __name__ == '__main__':
    from models.my_sql_driver import MySqlDriver
    my_sql_driver = MySqlDriver()
    # engine, session = my_sql_driver.connect_mysql()
    # engine, session = my_sql_driver.mysql_repeat(engine, session)
    question_sql = PaperCustomSql()
