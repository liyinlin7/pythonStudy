# from model import User
from flask import Blueprint
user_opt = Blueprint('user_opt', __name__)
# 查（按名字查）
@user_opt.route('/query_name/<user_name>', methods=['GET'])
def query_by_name(user_name):
    # users = User.query.filter(User.name == user_name).all()
    return 'user_opt'