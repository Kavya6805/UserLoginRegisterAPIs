from flask import Blueprint
from api.controllers import Login,Register,UserList,ForgetPassword

bp=Blueprint('api',__name__,url_prefix='/api')

bp.add_url_rule('/login',view_func=Login.login,methods=["POST"])
bp.add_url_rule('/registeruser',view_func=Register.register,methods=["POST"])
bp.add_url_rule('/userlist',view_func=UserList.userlist)
bp.add_url_rule('/forgetpassword',view_func=ForgetPassword.forgetpassword,methods=['POST'])
bp.add_url_rule('/reset-password/<reset_token>',view_func=ForgetPassword.resetpassword,methods=['POST'])
bp.add_url_rule('/verifylink/<reset_token>',view_func=ForgetPassword.verifylink,methods=['GET'])

