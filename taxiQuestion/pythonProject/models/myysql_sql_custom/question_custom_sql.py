from sqlalchemy import text
from models.mySql_mode import MySqlMode

class QuestionCustomSql(MySqlMode):

    # def question_select_custom_and(self, question_id=['1','2'], question_type:list=['1','2']):
    def question_select_custom_and(self, question_id: list=None, question_type: list=None):
        conditions = []
        params = {}
        # 添加条件到查询中
        if question_id is not None:
            # sql += " where question_id = :question_id"
            # params['question_id'] = question_id
            placeholders_id = ', '.join([':id' + str(i) for i in range(len(question_id))])
            conditions.append(" question_id IN (" + placeholders_id  + ")")
            # 为每个占位符添加对应的问题类型
            for i, id in enumerate(question_id):
                params['id' + str(i)] = id
        if question_type is not None:
            # sql += " and question_type = :question_type"
            # params['question_type'] = question_type
            placeholders_type = ', '.join([':type' + str(i) for i in range(len(question_type))])
            conditions.append(" question_type IN (" + placeholders_type + ")")
            # 为每个占位符添加对应的问题类型
            for i, type in enumerate(question_type):
                params['type' + str(i)] = type
        # 构建SQL查询
        sql = "SELECT * FROM questions"
        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        # 执行查询
        with self.session.begin():
            result = self.session.execute(text(sql), params)
            rows = result.fetchall()
            keys = result.keys()
        # 将结果转换为字典列表并打印
        result_dict = [dict(zip(keys, row)) for row in rows]
        print(result_dict)
        return result_dict
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
            placeholders_id = ', '.join([':id' + str(i) for i in range(len(question_id))])
            conditions.append(" questions.question_id IN (" + placeholders_id + ")")
            # 为每个占位符添加对应的问题类型
            for i, id in enumerate(question_id):
                params['id' + str( i )] = id
        if question_type is not None:
            # sql += " and question_type = :question_type"
            # params['question_type'] = question_type
            placeholders_type = ', '.join([':type' + str(i) for i in range( len( question_type ) )] )
            conditions.append(" questions.question_type IN (" + placeholders_type + ")" )
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
        with self.session.begin():
            result = self.session.execute( text( sql ), params )
            rows = result.fetchall()
            keys = result.keys()
        result_dict = [dict( zip( keys, row ) ) for row in rows]
        print( result_dict )
        return result_dict

    def question_types_groupBy(self):
        sql = "SELECT type FROM questions group by type"
        # query = self.session.query( Questions.type.distinct() ).group_by(Questions.type)
        with self.session.begin():
            result = self.session.execute( text( sql ) )
            rows = result.fetchall()
            keys = result.keys()
        # 将结果转换为字典列表并打印
        result_list = [ row[0] for row in rows]
        result_list.sort(key=len)
        return result_list

    def question_update_collect(self, question_id, collect):
        if question_id is not None and collect is not None:
            sql = f"update questions  set collect = :collect where question_id = :question_id;"
            # query = self.session.query( Questions.type.distinct() ).group_by(Questions.type)
            with self.session.begin():
                result = self.session.execute( text( sql ) , {"collect": collect, "question_id": question_id} )
                rows_affected = result.rowcount
                print(rows_affected)
                if rows_affected == 0:
                    return "没有更新任何记录"
                else:
                    return f"更新了{rows_affected}条记录"
        else:
            return "参数错误"


if __name__ == '__main__':
    from models.my_sql_driver import MySqlDriver
    my_sql_driver = MySqlDriver()
    # engine, session = my_sql_driver.connect_mysql()
    # engine, session = my_sql_driver.mysql_repeat(engine, session)
    question_sql = QuestionCustomSql()
    # question_sql.question_select_custom_and()
    question_sql.question_leftjoin_userAnswer_coustom_and()
