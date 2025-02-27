from api.models.userListModel import UserList
from common.common import apiResponse
from common.common import auth

# @auth
def userlist():
    try:
        userlist=UserList()
        data=userlist.userlist()
        data=[dict(row) for row in data]
        if data:
            return apiResponse(True,"Users Found!!",data)
        return apiResponse(False,"Users Not Found!!")
    except:
        return apiResponse(False,"Something Went Wrong!!",None)
