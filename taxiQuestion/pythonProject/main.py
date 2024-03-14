from flask import Flask, url_for
from flask import request
from controller.user_opt import user_opt
from controller.customer_opt import customer_opt
app = Flask(__name__)
# import config

# 注册蓝图，并指定其对应的前缀（url_prefix）
app.register_blueprint(user_opt, url_prefix="/user_opt")
app.register_blueprint(customer_opt, url_prefix="/customer_opt")
# 引入配置文件中的相关配置
# app.config.from_object(config)
# 配置db
# db.init_app(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login')
def login():
    return 'Login'

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
