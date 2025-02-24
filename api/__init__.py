from flask import Blueprint
from api.controllers import Login
from api.controllers import Register

bp=Blueprint('api',__name__,url_prefix='/api')

bp.add_url_rule('/login',view_func=Login.login,methods=["POST"])
bp.add_url_rule('/registeruser',view_func=Register.register,methods=["POST"])

