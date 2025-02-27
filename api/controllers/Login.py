from flask import jsonify, request
from api.models.loginModel import Login
from common.common import apiResponse
import re


def login():
    email = request.form['email']
    password = request.form['password']
    emailregex='^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$'

    print(re.search(emailregex,email))
    if re.search(emailregex,email):  
        login = Login()
        data = login.login(email, password)
        if data == 0:
            return apiResponse(False, "Wrong Password!!", "")
        elif data == -1:
            return apiResponse(False, "User Not Exist!!", "")
        else:
            return apiResponse(True, "User Authenticated Successfully", data)
     
    else:
        return apiResponse(False, "Enter Valid Email!!")

