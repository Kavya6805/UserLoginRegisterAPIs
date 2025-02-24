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
        if len(password)<8 | len(password)>12:
            login = Login()
            data = login.login(email, password)
            if data == "Wrong Password!!":
                return apiResponse(False, data, "")
            elif data == "User Not Exist!!":
                return apiResponse(False, data, "")
            else:
                return apiResponse(True, "User Authenticated Successfully", data)
        else:
            return apiResponse(False,"Password length must be in between 8 to 12")
    else:
        return apiResponse(False, "Enter Valid Email!!")

