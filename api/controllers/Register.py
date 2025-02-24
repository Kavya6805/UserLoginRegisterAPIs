from flask import request
from api.models.registerModel import Register
from common.common import apiResponse

def register():
    username=request.form['username']
    email=request.form['email']
    phone=request.form['phone']
    role=request.form['role']
    password=request.form['password']
    register=Register()
    data=register.register(username,email,phone,role,password)
    if data:
        message="User Created Successfully"
        return apiResponse(True,message,None)
    else:
        message="User With This Email Already Exists!!"
        return apiResponse(False,message,None)
