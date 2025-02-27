from flask import request
from api.models.registerModel import Register
from common.common import apiResponse
import re


def register():
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    role = request.form['role']
    password = request.form['password']
    register = Register()

    data = register.register(username, email, phone, role, password)
    print(data)
    if data:
        try:
            return apiResponse(True, data["message"], None)
        except:
            message = "User Created Successfully"
            return apiResponse(True,message)
    message = "User With This Email Already Exists!!"
    return apiResponse(False, message, None)
