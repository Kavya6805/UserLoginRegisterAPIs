from flask import jsonify,request
from api.models.loginModel import Login
from api.response import apiResponse


def login():
    username=request.form['username']
    password=request.form['password']
    login=Login()
    data=login.login(username,password)
    if data != None:
        return apiResponse(True,"User Authenticated Successfully",data)
    else:
        return apiResponse(False,"Username OR Password Wrong !!",None)
    
