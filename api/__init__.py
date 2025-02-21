from flask import Blueprint
from api.controllers import Login

bp=Blueprint('api',__name__,url_prefix='/api')

bp.add_url_rule('/login',view_func=Login.login,methods=["POST"])

