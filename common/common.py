from flask import Response,json,request
from functools import wraps
from flask import session 
import base64
from datetime import datetime
import re
# from app import bcrypt
import hashlib



def apiResponse(status=True,message="",data=None,http_status=200):
    response={
        "status":status,
        "message":message,
        "data":data
    }
    print(response)
    resp=Response(response=json.dumps(response),status=http_status,mimetype="application/json")
    print(resp)
    return resp

def auth(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.form['token']
        session_token=session['token']
        if token=='':
            return apiResponse(False,"Token is Missing!!")
        elif token!=session_token:
            return apiResponse(False,"Token is Wrong!!")
        else:
            return func(*args,**kwargs)
    return decorated

def generate_encrypted_string():
    current_time=str(datetime.now())
    current_time_bytes = current_time.encode("ascii")
    base64_bytes = base64.b64encode(current_time_bytes)
    base64_string = base64_bytes.decode("ascii")
    print(base64_bytes)
    print(base64_string)
    return base64_string
generate_encrypted_string()


def checkPasswordCredentials(password):
    upperregex = r"[A-Z]+"
    lowerregex = r"[a-z]+"
    digitregex = r"[0-9]+"
    specialregex = r"[@#!$%^&*()-+]+"
    if len(password) < 8 or len(password) > 12:
        return 0
    elif not (re.search(upperregex, password) and re.search(lowerregex, password) and re.search(digitregex, password) and re.search(specialregex, password)):
        return -1
    else:
        hashed_password=hashlib.md5(password.encode())
        print(hashed_password.hexdigest())
        return hashed_password.hexdigest()