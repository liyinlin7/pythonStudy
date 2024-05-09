# from model import User
from flask import Blueprint, jsonify
from models.mysql_sql_model.question_sql import QuestionSql
from models.myysql_sql_custom.question_custom_sql import QuestionCustomSql
from flask_cors import CORS,cross_origin
questions_opt = Blueprint('questions_opt', __name__)
question = QuestionSql()
question_cus = QuestionCustomSql()
# 查（按名字查）
@questions_opt.route('/id/<id>', methods=['GET'])
def query_by_name(id):
    # users = User.query.filter(User.name == user_name).all()
    return 'user_opt'

@questions_opt.route('/questionType', methods=['GET'])
@cross_origin(origin='http://127.0.0.1:8080', supports_credentials=True)
def query_by_type():
    # users = User.query.filter(User.name == user_name).all()
    result = question_cus.question_types_groupBy()
    if len(result) != 0:
        return jsonify( {'message': '成功', 'data': result} ), 200
    else:
        return jsonify( {'error': '查询失败或没有数据'} ), 404
