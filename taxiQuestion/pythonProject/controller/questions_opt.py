# from model import User
from flask import Blueprint, jsonify, request
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
        return jsonify( {'message': '查询失败或没有数据'} ), 200

@questions_opt.route('/updateCollect', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080', supports_credentials=True)
def query_update_collect():
    collect_value, question_id = None, None
    # 如果数据是通过表单传递的
    if request.method == 'POST' and request.form:
        collect_value = request.form.get( 'collect' )  # 假设表单中有一个名为 'collect' 的字段
        question_id = request.form.get( 'question_id' )  # 假设还有一个名为 'question_id' 的字段
    # 如果数据是通过 JSON 传递的
    elif request.method == 'POST' and request.is_json:
        data = request.get_json()
        collect_value = data.get( 'collect' )  # 假设 JSON 中有一个名为 'collect' 的键
        question_id = data.get( 'question_id' )  # 假设还有一个名为 'question_id' 的键
    result = question_cus.question_update_collect(collect = collect_value, question_id = question_id)
    if len(result) != 0:
        print(result)
        return jsonify( {'message': result} ), 200
    else:
        return jsonify( {'message': result} ), 404