from flask import jsonify, request
from api.models.loginModel import Login
from api.response import apiResponse


def login():
    username = request.form['username']
    password = request.form['password']
    login = Login()
    data = login.login(username, password)
    if data == "Wrong Password!!":
        return apiResponse(False, data, "")
    elif data == "User Not Exist!!":
        return apiResponse(False, data, "")
    else:
        return apiResponse(True, "User Authenticated Successfully", data)
