from flask import Flask, url_for
from flask import request, jsonify
from controller.user_opt import user_opt
from controller.questions_opt import questions_opt
from controller.customer_opt import customer_opt
from models.mysql_sql_model.users_sql import UsersSql
from flask_cors import CORS,cross_origin
from models.mysql_sql_model.question_sql import QuestionSql
import uuid
import json
app = Flask(__name__)
# CORS(app, resources={r"/login": {"origins": "http://127.0.0.1:8080"}})
CORS(app, resources={r"/*": {"origins": "*"}})
# import config

# 注册蓝图，并指定其对应的前缀（url_prefix）
app.register_blueprint(user_opt, url_prefix="/user_opt")
app.register_blueprint(customer_opt, url_prefix="/customer_opt")
app.register_blueprint(questions_opt, url_prefix="/questions_opt")
# 引入配置文件中的相关配置
# app.config.from_object(config)
# 配置db
# db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login', methods=['POST'])
@cross_origin(origin='http://127.0.0.1:8080', supports_credentials=True)
def login():
    dic = {
        'user_phone': [request.json.get('user_phone')],
        'password': [request.json.get('password')]
    }
    usersSql = UsersSql()
    user_bool = usersSql.users_select_and(dic)
    if user_bool == True:
        return jsonify( {'message': '成功', 'token': uuid.uuid4()} ), 200
    else:
        return jsonify( {'error': '用户账号密码错误'} ), 500

@app.route('/questions', methods=['GET'])
@cross_origin(origin='http://127.0.0.1:8080', supports_credentials=True)
def questions():
    # 从查询字符串中获取 page_size，并设置默认值
    page_size = request.args.get( 'page_size', type=int, default=10 )
    # 注意这里使用了 'pageIndex' 而不是 'page_index'（保持与查询字符串一致）
    page_index = request.args.get( 'pageIndex', type=int, default=1 )
    form_ = request.args.get( 'arges', default=None )
    __form = None
    print(form_)
    if form_ == '[object Object]':
        __form = {}
        print(111111)
    else:
        __form = json.loads(form_)
    print('__form', __form )
    dic = {
        'question_id': __form.get('question_id'),
        'question_type': __form.get('question_type'),
        'range': __form.get('range'),
        'collect': __form.get('collect'),
        'type': __form.get('type_op')
    }
    questionSql = QuestionSql()
    __result, total_count = questionSql.question_select_and(dic=dic, page_size=page_size, page_index=page_index)
    if len(__result) != 0:
        print('__result', __result)
        return jsonify( {'message': '成功', 'data': __result, 'total': total_count} ), 200
    else:
        return jsonify( {'message': '查询失败或没有数据'} ), 200

# @app.route('/user/<username>')
# def show_user_profile(username):
#     # show the user profile for that user
#     return 'User %s' % username
#
#
# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return 'Post %d' % post_id
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         # do_the_login()
#         pass
#     else:
#         # show_the_login_form()
#         pass


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
