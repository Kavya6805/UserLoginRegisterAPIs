from flask import Response,json 

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