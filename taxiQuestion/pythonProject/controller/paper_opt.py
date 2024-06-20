# from model import Customer
from flask import request
from flask import Blueprint, jsonify
from models.mysql_sql_model.paper_sql import PaperSql
from models.myysql_sql_custom.paper_custom_sql import PaperCustomSql
from models.myysql_sql_custom.question_custom_sql import QuestionCustomSql
from models.myysql_sql_custom.paper_question_custom_sql import PaperQuestionCustomSql
from models.my_sql_driver import MySqlDriver
import json
import time
import uuid
from flask_cors import CORS,cross_origin
paper_opt = Blueprint('paper_opt', __name__)
paperCustomSql = PaperCustomSql()
questionCustomSql = QuestionCustomSql()
paperQuestionCustomSql = PaperQuestionCustomSql()

# 查（按 id 查）
@paper_opt.route('/query_id', methods=['GET'])
def query_by_id():
    customer_id = request.args.get( 'customer_id' )  # 从GET参数中获取customer_id
    # customer = Customer.query.filter(Customer.id == customer_id).first()
    return 'customer_opt'

# 根据 题目分类查询
@paper_opt.route('/paperSelect', methods=['GET'])
@cross_origin(origin='http://127.0.0.1:8080', supports_credentials=True)
def query_select_paper():
    page_size = request.args.get( 'page_size', type=int, default=10 )
    # 注意这里使用了 'pageIndex' 而不是 'page_index'（保持与查询字符串一致）
    page_index = request.args.get( 'pageIndex', type=int, default=1 )
    form_ = request.args.get( 'arges', default=None )
    __form = None
    if form_ == '[object Object]' or form_ == 'undefined':
        __form = {}
    elif form_ is None:
        __form = {}
    else:
        __form = json.loads( form_ )
    dic = {
        'paperId': __form.get( 'paperId' ),
        'paperName': __form.get( 'paperName' ),
        'paperType': __form.get( 'paperType' ),
        'paperRange': __form.get( 'paperRange' ),
        'paperQuestionType': __form.get( 'paperQuestionType' )
    }
    paperSql = PaperSql()
    __result, total_count = paperSql.paper_select_and( dic=dic, page_size=page_size, page_index=page_index )
    if len( __result ) != 0:
        return jsonify( {'message': '成功', 'data': __result, 'total': total_count} ), 200
    else:
        return jsonify( {'message': '查询失败或没有数据'} ), 200

@paper_opt.route('/paperInstall', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080', supports_credentials=True)
def query_install_paper():
    paper_id = uuid.uuid4()
    paper_name, paper_type, paper_range, paper_question_type = None, None, None, None
    # 如果数据是通过表单传递的
    if request.method == 'POST' and request.form:
        print(type(request.form))
        paper_name = request.form.get( 'paperName' )  # 假设表单中有一个名为 'paperName' 的字段
        paper_type = request.form.get( 'paperType' )  # 假设还有一个名为 'paperType' 的字段
        paper_range = request.form.get( 'paperRange' )  # 假设还有一个名为 'paperRange' 的字段
        paper_question_type = request.form.get( 'paperQuestionType' )  # 假设还有一个名为 'paperQuestionType' 的字段
    # 如果数据是通过 JSON 传递的
    elif request.method == 'POST' and request.is_json:
        data = request.get_json()
        paper_name = data.get( 'paperName' )  # 假设 JSON 中有一个名为 'collect' 的键
        paper_type = data.get( 'paperType' )  # 假设 JSON 中有一个名为 'collect' 的键
        paper_range = data.get( 'paperRange' )  # 假设 JSON 中有一个名为 'collect' 的键
        paper_question_type = data.get( 'paperQuestionType' )  # 假设还有一个名为 'question_id' 的键
    __result = paperCustomSql.paper_install_custom(paper_id=paper_id, paper_name=paper_name,
                                                                    paper_type=paper_type, paper_range=paper_range,
                                                                    paper_question_type=paper_question_type)
    err_count = 0
    if len( __result ) != 0:
        result_dict = questionCustomSql.question_select_custom_and(question_type=paper_question_type, type_=paper_type, range_=paper_range)  # 查询试卷类型的所有题目
        if result_dict is not None:
            for i in range(len(result_dict)):
                paper_id_ = paper_id
                question_id = result_dict[i]['question_id']
                question_answer = result_dict[i]['question_answer']
                result_str = paperQuestionCustomSql.paper_question_install_custom(paper_id=paper_id_, question_id=question_id, question_answer=question_answer)
                if result_str == f"题目试卷关联插入{question_id}失败":
                    err_count += err_count+1
        if err_count == 0:
            return jsonify( {'message': __result + ',试卷题目关联表插入成功'}), 200
        else:
            return jsonify( {'message': __result + f'，但是题目id有{err_count}条没有插入到试卷题目关联表'} ), 200
    else:
        return jsonify( {'message': __result} ), 404

@paper_opt.route('/deletePaper', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080', supports_credentials=True)
def query_delete_paper():
    paperId = None
    # 如果数据是通过表单传递的
    if request.method == 'POST' and request.form:
        paperId = request.form.get( 'paperId' )  # 假设表单中有一个名为 'collect' 的字段
    # 如果数据是通过 JSON 传递的
    elif request.method == 'POST' and request.is_json:
        data = request.get_json()
        paperId = data.get( 'paperId' )  # 假设 JSON 中有一个名为 'collect' 的键
    result = paperCustomSql.paper_delete(paperId)
    result_ = paperCustomSql.paper_question_delete(paperId)
    # print(result)
    if len( result ) != 0 and len( result_ ) != 0:
        return jsonify( {'message': result} ), 200
    else:
        return jsonify( {'message': "没有删除任何记录"} ), 404

@paper_opt.route('/selectPaperQuestion', methods=['GET'])
@cross_origin(origin='http://127.0.0.1:8080', supports_credentials=True)
def query_select_paper_question():
    paperId = request.args.get( 'paperId' )
    questionBool = request.args.get( 'questionBool' )
    questionId = request.args.get( 'questionId' )
    __result, total_count = paperQuestionCustomSql.paper_question_select( paperId=paperId, questionBool=questionBool, questionId=questionId )
    # print(__result)
    if len( __result ) != 0:
        return jsonify( {'message': '成功', 'data': __result, 'total': total_count} ), 200
    else:
        return jsonify( {'message': '查询失败或没有数据'} ), 200

@paper_opt.route('/updatePaperQuestion', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080', supports_credentials=True)
def query_update_paper_question():
    paperId = None
    userAnswer = None
    questionId = None
    questionBool = None
    # 如果数据是通过表单传递的
    if request.method == 'POST' and request.form:
        paperId = request.form.get( 'paperId' )  # 假设表单中有一个名为 'collect' 的字段
        userAnswer = request.form.get( 'userAnswer' )  # 假设表单中有一个名为 'collect' 的字段
        questionId = request.form.get( 'questionId' )  # 假设表单中有一个名为 'collect' 的字段
        questionBool = request.form.get( 'questionBool' )  # 假设表单中有一个名为 'collect' 的字段
    # 如果数据是通过 JSON 传递的
    elif request.method == 'POST' and request.is_json:
        data = request.get_json()
        paperId = data.get( 'paperId' )  # 假设 JSON 中有一个名为 'collect' 的键
        userAnswer = data.get( 'userAnswer' )  # 假设 JSON 中有一个名为 'collect' 的键
        questionId = data.get( 'questionId' )  # 假设 JSON 中有一个名为 'collect' 的键
        questionBool = data.get( 'questionBool' )  # 假设 JSON 中有一个名为 'collect' 的键
    print(paperId, userAnswer, questionId, questionBool)
    if paperId is not None and userAnswer is not None and questionId is not None and questionBool is not None:
        result = paperQuestionCustomSql.paper_question_update(paperId=paperId, questionId=questionId, userAnswer=userAnswer, questionBool=questionBool)
        # print(result)
        if len( result ) != 0:
            return jsonify( {'message': result} ), 200
        else:
            return jsonify( {'message': '提交答案失败'} ), 404
    else:
        return jsonify( {'message': '参数错误'} ), 500