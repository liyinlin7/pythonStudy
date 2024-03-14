# from model import Customer
from flask import Blueprint
customer_opt = Blueprint('customer_opt', __name__)

# 查（按 id 查）
@customer_opt.route('/query_id/<customer_id>')
def query_by_id(customer_id):
    # customer = Customer.query.filter(Customer.id == customer_id).first()
    return 'customer_opt'