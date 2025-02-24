from flask import Response,json,request
from functools import wraps
from flask import session 

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