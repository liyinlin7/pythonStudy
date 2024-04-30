# from model import Customer
from flask import request
from flask import Blueprint, jsonify
from models.mysql_sql_model.question_sql import QuestionSql
from models.my_sql_driver import MySqlDriver
customer_opt = Blueprint('customer_opt', __name__)

# 查（按 id 查）
@customer_opt.route('/query_id', methods=['GET'])
def query_by_id():
    customer_id = request.args.get( 'customer_id' )  # 从GET参数中获取customer_id
    # customer = Customer.query.filter(Customer.id == customer_id).first()
    return 'customer_opt'

# 根据 题目分类查询
@customer_opt.route('/type', methods=['GET'])
def query_by_type():
    type__ = ['运价与计程计价设备使用知识', '车辆服务要求', '行车安全与突发情况处置', '节能与环保知识', '自我安全防范',
            '精神文明', '社会责任与职业道德',
            '特殊人员服务与服务禁忌', '法律法规', '服务评价与投诉处理', '服务规范、职业道德、安全营运', '服务规范',
            '服务要求',
            '应急保障、消防和乘客救护基础知识', '常见危险品的基本知识', '实操', '安全运营生理与心理知识',
            '地理地标、营运线路', '人文景观', '交通事故处理']
    type_value_str = request.args.get('type')
    type_value = type_value_str.split( ',' ) if type_value_str is not None else []
    question_id_str = request.args.get( 'question_id' )
    question_id = question_id_str.split( ',' ) if question_id_str is not None else []
    question_type_str = request.args.get('question_type')
    question_type = question_type_str.split( ',' ) if question_type_str is not None else []
    if len(type_value) > 1 or len(question_id) > 1 or len(question_type) > 1:
        return jsonify( {'error': '参数数量超过1个'} ), 500
    dic = {
        "type" : type_value,
        "question_id" : question_id,
        "question_type" : question_type
    }
    # if type_value not in type__:
    #     return jsonify( {'error': 'Invalid type_value'} ), 400
    customer = QuestionSql().question_select_and(dic)
    return customer


